#include<lpc21xx.h>   

void Uart0Init (void)            
{                   
   PINSEL0 = 0x00000005;                               
   U0LCR = 0x83;                              
   U0DLL = 97;                           
   U0LCR = 0x03; 
	 IO0DIR = 0x00000017; 
}
   
void Uart0PutCharacter (unsigned char ch)    
{                    
    U0THR = ch;
  while (!(U0LSR & 0x20));
}

void  Uart0PutS(unsigned char *str)  
{  
while(*str)
{  
     Uart0PutCharacter(*str++);     
}
}
unsigned char Uart0GetCharacter (void)     
{            
 while (!(U0LSR & 0x01));
 return (U0RBR);
}
void delay();
int main()
{
unsigned char a;
Uart0Init();
while(1)
{
	if ( IO0PIN & (1<<1) )	
		{
			IOSET0 =0XfffffFFF;
			a=Uart0GetCharacter(); // Get the character
			Uart0PutCharacter(a);  // Put the character
			delay();
		}
		else 
		{
			IOCLR0 =0XFFFfffff;	
			delay();
		}		

}
}
void delay()
{
    unsigned int i;
    for(i=0;i<30000;i++);
}