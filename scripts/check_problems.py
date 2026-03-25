#!/usr/bin/env python3
import os

def check_existing_problems():
    dirs = []
    for item in os.listdir('.'):
        if os.path.isdir(item) and (item.startswith('1.') or item.startswith('2.') or 
                                   item.startswith('3.') or item.startswith('4.') or 
                                   item.startswith('5.') or item.startswith('6.') or 
                                   item.startswith('7.') or item.startswith('8.') or 
                                   item.startswith('9.') or item.startswith('10.') or 
                                   item.startswith('11.') or item.startswith('12.') or 
                                   item.startswith('13.') or item.startswith('14.') or 
                                   item.startswith('15.') or item.startswith('16.') or 
                                   item.startswith('17.') or item.startswith('18.') or
                                   item.startswith('19.') or item.startswith('20.')):
            dirs.append(item)
    
    dirs.sort()
    
    print('Existing problems:')
    for i, d in enumerate(dirs, 1):
        print(f'{i:2d}. {d}')
    
    print(f'\nTotal problems: {len(dirs)}')
    print(f'Last problem: {dirs[-1] if dirs else "None"}')
    
    return dirs

if __name__ == "__main__":
    check_existing_problems()
