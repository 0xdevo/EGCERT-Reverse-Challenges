# strings writeup

lets run the program in IDA and look at the strings

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/strings/1.png)

"W3lc0m3_2_EG-ctf"  this look like interstring string to try to submit

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/strings/2.png)

this is code that take out input and save it into "v102" so lets change this variable into "first_pass" ...

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/strings/3.png)

this is the algorithm that encrybt the first_pass by taking the hex value of the char and sum it with 3 

so for examble if the char was "A" it will be "D"

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/strings/4.png)

second password 

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/strings/5.png)
![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/strings/6.png)

after submiting the second password it combine the first_password and the second together

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/strings/7.png)

here it compare the first four char into our input in reversed order which is "iwf0" with the first first four char of "W3lc0m3_2_EG-ctf" in reversed of which is "cl3W"  and if the compare is right it will move into nex four char

so lets convert the first input to right one
"W3lc0m3_"  will be "T0i\`-3j0\"  and after revese it will be "\0j-\`i0T"

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/strings/8.png)

as you can see this input "\0j-\`i0T"  become "W3lc0m3_"

and the "A" char of the second password converted into > , but after trying to generate the right value using this sequence it fail  so i brute-force  the char until i got the right char

which is "5bZX0|ky"

not lets run the program using this values and see

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/strings/9.png)
