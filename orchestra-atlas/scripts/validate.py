#!/usr/bin/env python3
"""Validate Orchestra Atlas structured data using Python standard library only."""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FIELDS={'id','type','category','title','english','subtitle','tags','range','character','use','tip','related','icon'}
CATEGORIES={'strings','woodwinds','brass','orchestration'}
def main():
    errors=[]
    try: entries=json.loads((ROOT/'content/entries.json').read_text(encoding='utf-8'))
    except (OSError,json.JSONDecodeError) as e: print('FAIL:',e);return 1
    if not isinstance(entries,list) or not entries: print('FAIL: expected nonempty array');return 1
    ids=[]
    for index,e in enumerate(entries):
        key=f'entry[{index}]'
        if not isinstance(e,dict): errors.append(f'{key}: must be object');continue
        missing=FIELDS-set(e);extra=set(e)-FIELDS
        if missing: errors.append(f'{key}: missing {sorted(missing)}')
        if extra: errors.append(f'{key}: unexpected {sorted(extra)}')
        if not FIELDS<=set(e):continue
        if not isinstance(e['id'],str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',e['id']):errors.append(f'{key}: invalid id')
        ids.append(e['id'])
        if e['type'] not in {'instrument','technique'}:errors.append(f'{key}: invalid type')
        if e['category'] not in CATEGORIES:errors.append(f'{key}: invalid category')
        if (e['type']=='technique')!=(e['category']=='orchestration'):errors.append(f'{key}: technique category mismatch')
        for field in ['title','english','subtitle','range','character','use','tip','icon']:
            if not isinstance(e[field],str) or not e[field].strip():errors.append(f'{key}: {field} must be nonempty string')
        for field in ['tags','related']:
            if not isinstance(e[field],list) or any(not isinstance(v,str) or not v.strip() for v in e[field]):errors.append(f'{key}: {field} invalid')
        if isinstance(e['tags'],list) and not e['tags']:errors.append(f'{key}: tags must not be empty')
    if len(ids)!=len(set(ids)):errors.append('duplicate IDs')
    for e in entries:
        if not isinstance(e,dict) or not isinstance(e.get('related'),list):continue
        for ref in e['related']:
            if ref not in ids:errors.append(f"{e.get('id')}: related ID '{ref}' not found")
            if ref==e.get('id'):errors.append(f"{ref}: cannot relate to itself")
    if errors:
        for e in errors:print('FAIL:',e)
        return 1
    print(f'PASS: {len(entries)} entries valid; unique IDs, required fields and related links OK.')
    return 0
if __name__=='__main__':sys.exit(main())
