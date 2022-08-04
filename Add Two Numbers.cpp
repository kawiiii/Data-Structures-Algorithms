class Solution {
public:
    
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* final_list = new ListNode(0);
        ListNode* finalNode = final_list;
        int carry = 0;
        
        while (l1||l2){
            if (l1){
                carry+= l1->val;
                l1=l1->next;
            }
            
            if (l2){
                carry+= l2->val;
                l2=l2->next;
            }
            
            final_list-> val = carry %10;
            carry/=10;
            
            if (l1||l2||carry){
                final_list->next = new ListNode(carry);
                final_list = final_list->next;
            }
            
            
        }
        return finalNode;
    }
};
