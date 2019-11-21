# snowball

lets run the program in ida

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/snowball/1.png)

then add a brakpoint , and run the program in linux using  ida linux server 

then send a "BBBBB" as an argument 

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/snowball/3.png)


here it moves our input into "var_40" , so lets rename it to "input" ....

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/snowball/4.png)


here there is two things , first it check if the length of our input is less than or equal to 4 , the other is that it combining each char in our input into one variabl "var_50"

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/snowball/5.png)

here it move the result of compination into RAX  which is "14A" 

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/snowball/6.png)

here it compar our input with "14C" .....


![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/snowball/7.png)

this is the bad message

so lets calculate the right input

if we divide the the right input which is "14C" into 5

14Ch / 5h = 42

42h * 5h = 14A   and this is the value that we submit , so to  get the right value we need to replace the last "B" from the input with something else

like "C" 

so
42h * 4h = 108h  + 44h = 14Ch ....

![1](https://raw.githubusercontent.com/devodevo1/EGCERT-Reverse/master/snowball/8.png)
