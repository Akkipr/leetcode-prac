// Last updated: 5/10/2026, 12:03:10 AM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* insertionSortList(struct ListNode* head) {

    struct ListNode *j;
    j=head;
    struct ListNode *i;
    i=j->next;
    struct ListNode *prev = NULL;
    while (i!=NULL) {
        struct ListNode *remo1;
        remo1=head;
        struct ListNode *remo2;
        remo2=head->next;
        while (remo2 != i) {
            remo1=remo1->next;
            remo2=remo2->next;
        }
        remo2=remo2->next;
        remo1->next = remo2;
        j=head;

        while (j != NULL && j != i) {
            if (i->val <= j->val) { 
                break;          
            }
            else {
                prev = j;
                j = j->next;
            }
        }
        struct ListNode *temp = remo2;
        if (prev == NULL) {
            head=i;
            i->next = j;
        }else {
            prev->next=i;
            i->next = j;
        }
        i=temp;
        prev=NULL;
    }
    return head;


}