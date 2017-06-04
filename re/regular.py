import re
print(
    re.match(r'(^\w+\.)*\w+@{1}\w+(\.{1}\w+)+$', 'bill.gates@microsoft.com.cn')
    )
print(
    re.match(r'^(\w+\.)*\w+@{1}\w+(\.{1}\w+)+$', '742790905.huu@qq.com.cn.net')
    )
regu=re.match(r'^(\<{1}[A-Z]{1}[a-z]*\s[A-Z]{1}[a-z]*\>{1})?\s*(\w+\.)*\w+@{1}\w+(\.{1}\w+)+$', '<Tom Paris> tom@voyager.org')
print(
regu.group(1)
)


