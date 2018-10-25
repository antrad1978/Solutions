A simple basic solution to implement a licensing server.
This sample uses Django, Admin and Rest Framework.
Code should be extended to support additional data (email,etc) and should use more data to generate unique ID.
Even it should be added a protection against VMs.
You can reset Django Admin password via "changepassword" option.

a C sample code:

int swallow_redpill () {
   unsigned char m[2+4], rpill[] = "\x0f\x01\x0d\x00\x00\x00\x00\xc3";
   *((unsigned*)&rpill[3]) = (unsigned)m;
   ((void(*)())&rpill)();
   return (m[5]>0xd0) ? 1 : 0;
 } 
