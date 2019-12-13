
writeup

writeup
hello , this is devo

this exe is build using GO language , you will notice that if you look at the strings and by the strange functions name in IDA
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/1.png)
Now if we run the program it will ask for two argument  , so let’s go to the debugger and look at what it does with this arguments
The functions contain ‘main_main’ , ‘main_not_log’ and ‘main_log’
I looked at ‘main_main’ and didn’t find any thing useful  , ‘main_not_log’ this contains the important functions and ‘main_log’ it run a powershell but it doesn’t important
Now let’s run the program with this arguments ‘devo’ and ‘devo’  and put a breakpoint in ‘main_not_log’ function
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/2.png)
Here it add the argument length in ‘rbx’ which is 8 , then loop throw them
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/3.png)</br>
This function ‘runtime_intstring’ get the first char from the first input which is ‘d’
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/4.png)</br>
Here it get the last char from the second input wich is ‘o’
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/5.1.png)</br>
This function ‘runtime_concatstring2’ concat  the ‘d’ and ‘o’ together  
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/5.2.png)</br>
This function ‘crypto_sha256___digest__Sum’ encrypt the  ‘do’ with sha256 algorithm  to be compared with the first and last char of the flag

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/6.png)</br>
This function compare the encrypted characters from our input with the first and last char from the flag 
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/7.png)</br>
Here the compare is happen 
It compare our input
'ac0b52a2ae6ef99999bc08fb31e19188bf0085a4614204068e677e140e1458be' =  ‘do’</br>
with this hash</br>
d72b887f3e2ab73218b300e417f35f36bc6750e57d6188a3e269d6bd1134c7bad</br>
but this hash cannot be decrypted because it had an additional character at the end which is ‘d’</br>
so after removing it </br>
d72b887f3e2ab73218b300e417f35f36bc6750e57d6188a3e269d6bd1134c7ba = ‘E}’</br>
the first and last char from the flag</br>
so we can repeat this method to collect the flag</br>
for example the second hash of the flag will be</br>
954edbbc5f5c2074629bd1c9f2d76ebffd42111688e6782d8ebe3a1e28d08652 = ‘Ge’</br>
so combining them will be  ‘EGe}’</br>
And so on until you get the flag , but if the length of our input doesn’t match the length of the flag so after couple of times the program will exist , so I try a lot of times with different lengths  until I got the flag
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/8.png)

another solution is to get all the hashes automatically from memory then decrypt it

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/9.png)

at line 51 it start to fill the variable 'address_of_flag_hash' with the hashes addresses

what we need to do is to get the address of first element then loop throw all of the element’s to extract the hashes

the base address that we will start from is 0x7301E0 which is the address of "qword_7301E0"

then we start the loop from that address with step of 0x10 , extract the address of the hash then extract the hash itself

this is python script to do that

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/10.png)</br>
Dword(ptr)  extract the dword value from specific address</br>
GetManyBytes  extract multiple values from specific address , the 64 is length of the hash

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/11.png)

copy the hashes into file then decrypt them using this python script

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/12.png)

and here is the flag

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/home/13.png)
