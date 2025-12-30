// Last updated: 12/30/2025, 4:58:02 AM
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *currentValue = list1;
    struct ListNode *nextValue = list1;
    struct ListNode *subIn = list2;

    if (currentValue == NULL && subIn == NULL) {
        return NULL;
    }

    if (currentValue == NULL && subIn != NULL) {
        return subIn;
    }

    if (currentValue != NULL && subIn == NULL) {
        return currentValue;
    }

    if (subIn == NULL) {
        return NULL;
    }

    nextValue = nextValue->next;

    while (subIn != NULL && currentValue!=NULL ) {
        if (nextValue!=NULL) {
            if (currentValue->val > subIn->val || nextValue->val < subIn->val) {
                    currentValue = currentValue->next;
                    nextValue = nextValue->next;
                }
            }
        if (nextValue != NULL) {
            if (currentValue->val <= subIn->val && nextValue->val >= subIn->val) {
                struct ListNode *temp = NULL;
                temp = malloc(sizeof(struct ListNode));
                if (temp==NULL) {
                    return NULL;
                }
                temp->val = subIn->val;
                temp->next = nextValue;
                currentValue->next = temp;

                currentValue = currentValue->next;

                

                subIn = subIn->next;
            }
        }
        if (nextValue == NULL) {
            if (currentValue->val <= subIn->val) {
                struct ListNode *temp = NULL;
                temp = malloc(sizeof(struct ListNode));
                if (temp==NULL) {
                    return NULL;
                }
                temp->val = subIn->val;
                temp->next = NULL;
                currentValue->next = temp;

                currentValue = currentValue->next;

                

                subIn = subIn->next;
            }
            else if (currentValue->val > subIn->val) {
                struct ListNode *temp = NULL;
                temp = malloc(sizeof(struct ListNode));
                if (temp==NULL) {
                    return NULL;
                }
                temp->val = subIn->val;
                temp->next = list1;
                currentValue = temp;
                list1 = currentValue;
                nextValue = currentValue->next;


                

                subIn = subIn->next;
            }
        }
    }

    currentValue = list1;
    return currentValue;  
}