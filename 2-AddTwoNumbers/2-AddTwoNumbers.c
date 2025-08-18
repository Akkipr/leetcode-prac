/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 #include <math.h>
 #include <stdint.h>

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode *p=NULL;
    struct ListNode *q=NULL;
    struct ListNode *r=NULL;
    struct ListNode *s=NULL;

    p=l1;
    q=l2;
    int carryout = 0;
    int num1 = 0;

    while (p!=NULL && q!=NULL) {
        num1 = p->val+q->val+carryout;
        r=(struct ListNode *)calloc(1, sizeof(struct ListNode));

        carryout=0;
        if ((num1/10) > 0) {
            carryout=1;
            num1=num1-10;
        }

        r->val = num1;
        r->next = NULL;

        if (s==NULL) {
            s=r;
        }else {
            r->next = s;
            s=r;
        }
        p=p->next;
        q=q->next;
    }

    if (q==NULL) {
        while (p!=NULL) {
            num1 = p->val+carryout;
            r=(struct ListNode *)calloc(1, sizeof(struct ListNode));

            carryout=0;
            if ((num1/10) > 0) {
                carryout=1;
                num1=num1-10;
            }

            r->val = num1;
            r->next = NULL;

            if (s==NULL) {
                s=r;
            }else {
                r->next = s;
                s=r;
            }
            p=p->next;
        }
    } else {
        while (q!=NULL) {
            num1 = q->val+carryout;
            r=(struct ListNode *)calloc(1, sizeof(struct ListNode));

            carryout=0;
            if ((num1/10) > 0) {
                carryout=1;
                num1=num1-10;
            }

            r->val = num1;
            r->next = NULL;

            if (s==NULL) {
                s=r;
            }else {
                r->next = s;
                s=r;
            }
            
            q=q->next;
        }
    }

    

    p=NULL;
    q=s;
    r=s->next;
    while (r!=NULL) {
        q->next=p;
        p=q;
        q=r;
        r=r->next;
    }
    s=q;
    s->next=p;

    p=NULL;
    p=s;
    if (carryout==1) {
        while (p->next!=NULL) {
            p=p->next;
        }
        r=(struct ListNode *)calloc(1, sizeof(struct ListNode));
        r->val = 1;
        r->next = NULL;
        p->next=r;

    }
    
    return s;

}

