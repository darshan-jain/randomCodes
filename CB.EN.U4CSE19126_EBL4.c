#include<lpc21xx.h>   

// Intializing Interface
void Uart0Init (void)            
{                   
   PINSEL0 = 0x00000005;                               
   U0LCR = 0x83;                              
   U0DLL = 97;                           
   U0LCR = 0x03; 
	 IO0DIR = 0x00000017; // PIN 17 FOR GPIO
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
int main()
{
unsigned char a;
Uart0Init();
while(1)
{
	if ( IO0PIN & (1<<1) )	
		{
			IO0CLR = 0x00000001;
			a=Uart0GetCharacter(); // Get the character
			Uart0PutCharacter(a);  // Put the character
		}
		else 
		{
			IO0SET = 0x00000001;	
		}		

}
}