import re
for i in range(int(raw_input())):
    M=raw_input().strip()
    pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',M)
    if pre_match:
        process= "".join(pre_match.group(0).split('-'))
        final_match = re.search(r'(\d)\1{3,}',process)
        print'Invalid' if final_match else 'Valid'
    else:
        print 'Invalid'    
