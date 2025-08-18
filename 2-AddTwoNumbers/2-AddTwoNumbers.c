// Last updated: 8/18/2025, 3:36:31 AM
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
    long long num2 = 0;

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

    struct ListNode *a=NULL;
    struct ListNode *b=NULL;
    struct ListNode *c=NULL;

    a=NULL;
    b=s;
    c=s->next;
    while (c!=NULL) {
        struct ListNode *temp=NULL;
        temp=b;
        b->next=a;
        a=temp;
        b=c;
        c=c->next;
    }
    s=b;
    s->next=a;

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

