# ── 1. Two Sum ──────────────────────────────────────────────
def twoSum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i

print(twoSum([2,7,11,15], 9))       

# ── 217. Contains Duplicate ──────────────────────────────────
def containsDuplicate(nums):
    return len(nums) != len(set(nums))

print(containsDuplicate([1,2,3,1]))  
print(containsDuplicate([1,2,3,4]))  

# ── 121. Best Time to Buy and Sell Stock ─────────────────────
def maxProfit(prices):
    low, profit = float('inf'), 0
    for p in prices:
        low = min(low, p)
        profit = max(profit, p - low)
    return profit

print(maxProfit([7,1,5,3,6,4]))      

# ── 125. Valid Palindrome ────────────────────────────────────
def isPalindrome(s):
    s = [c.lower() for c in s if c.isalnum()]
    return s == s[::-1]

print(isPalindrome("kabak"))  
print(isPalindrome("mehmet"))                      

# ── 21. Merge Two Sorted Lists ───────────────────────────────
class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n

def mk(vs):
    h=c=ListNode(vs[0])
    for v in vs[1:]: c.next=ListNode(v); c=c.next
    return h

def mergeTwoLists(l1, l2):
    if not l1 or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)
    return l1

h = mergeTwoLists(mk([1,2,4]), mk([1,3,4]))
r = []
while h: r.append(h.val); h = h.next
print(r) 

# ── 141. Linked List Cycle ───────────────────────────────────
class ListNode:
    def __init__(self, v=0, n=None): self.val=v; self.next=n

def mk(vs):
    h=c=ListNode(vs[0])
    for v in vs[1:]: c.next=ListNode(v); c=c.next
    return h

def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast: return True
    return False

print(hasCycle(mk([1,2,3])))        
a = mk([1,2,3]); a.next.next.next = a.next
print(hasCycle(a))                   

# ── 20. Valid Parentheses ────────────────────────────────────
def isValid(s):
    stack, m = [], {')':'(', ']':'[', '}':'{'}
    for c in s:
        if c in m:
            if not stack or stack[-1] != m[c]: return False
            stack.pop()
        else:
            stack.append(c)
    return not stack

print(isValid("()[]{}"))  
print(isValid("(]"))      

# ── 150. Evaluate Reverse Polish Notation ───────────────────
def evalRPN(tokens):
    stack = []
    ops = {'+': lambda a,b: a+b, '-': lambda a,b: a-b,
           '*': lambda a,b: a*b, '/': lambda a,b: int(a/b)}
    for t in tokens:
        if t in ops:
            b, a = stack.pop(), stack.pop()
            stack.append(ops[t](a, b))
        else:
            stack.append(int(t))
    return stack[0]

print(evalRPN(["2","1","+","3","*"]))  
print(evalRPN(["4","13","5","/","+"]))  

# ── 704. Binary Search ───────────────────────────────────────
def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target: return mid
        elif nums[mid] < target: l = mid + 1
        else: r = mid - 1
    return -1

print(search([-1,0,3,5,9,12], 9))   
print(search([-1,0,3,5,9,12], 2))   

# ── 104. Maximum Depth of Binary Tree ───────────────────────
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val; self.left=left; self.right=right

def maxDepth(root):
    if not root: return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(maxDepth(root)) 