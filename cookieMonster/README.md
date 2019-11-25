
cookieMonster write-up

First we have the TLS callback  ,this used to detect if you run the app in debugger or not So let's patch it so we can avoid any issue Change this "jnz" to "jz" </br>
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/1.png)
</br>This too</br>
![2](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/2.png)
</br>Here it moves some values that will be used to generate the flag</br>
![3](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/3.png)
</br>To find the main function i look at the strings and jump into the function that contains "EGCTF" keyword

when we run this app it start looking for folder called "th3_Pl4tE" open it and start to gather the existing files you can see this behavior using "Procmon"

So let’s create this folder and create 5 files with random names and we will know why 5 later
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/4.png)
</br>Now let’s go to the function that generate part of the flag
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/5.png)
i called it generate_1</br>
mov cl,[esi+edx]</br>
This takes the first char of the "abcdef" file and save it into cl register</br>
lea edx,[edx+1]</br>
This points to the place where the generated chars will be saved</br>
inc eax</br>
This will increment the eax value with "1" , BTW the eax value is "6f" so it will be 70</br>
xor cl,al</br>
Here it will xor the value "70" with the first char which is "61"</br>
mov [edx-1],cl</br>
It move the result into this place "[edx-1]"</br>
sub edi,1</br>
Decrement the edi by 1 </br>
And if you look at the "edi" value it will equal to 0xC and out filename is only 0x6 so let’s modify it and continue</br>
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/6.png)
the “unk_1338520” contain the right charters but encoded and it compare it with the generated charters of the first file
so in order to get the right char we need to invert the xor formula
we know that the generate function start from 70 after increment
so
70 xor 1D = m
71 xor 10 = a
72 xor 0 = r
so the right word will be “marshmallow “

after the comparison is finished it going to generate the second part of the flag , i called the function “generate_2”
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/7.png)
what this function dose is take the third char of "Monster" word which is s = 0x73 and increment it with 1 then xor it with the first char of the second file it continue do this 9 times which is the length of the file name
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/8.png)
here it compare the encoded char with the right one so let’s invert the right chars to get the original value
74 xor 17 = c
75 xor 45 = 0
76 xor 19 = o
And the right word is "c0ocKi3z_"
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/9.png)
This is the last function that generate the flag so by now it should be understood how to get the flag from this one
so the right value is "m1Lk"
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/10.png)
if we continue until this part will see that i compare the [ebp+var_338] with 3  , here it check if the first three files were correct of not

the second compare is
cmp [ebp+var_344],eax
This check if eax equal to 0 or not , and eax is equal to zero because it's value decrement 5 time which is number of our files 

continue
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/11.png)
and
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/cookieMonster/12.png)
