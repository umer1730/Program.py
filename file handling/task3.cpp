#include<iostream>
#include<fstream>
using namespace std;
void inputsignup(string username,string password);
void storesignup(string username,string password);
main() 
{
    string username;
    string password;
    inputsignup(username,password);
    storesignup(username,password);
    return 0;
}
void inputsignup(string username,string password) 
{
    cout<<"Enter username: ";
    cin>>username;
    cout<<"Enter password: ";
    cin>>password;
}
void storesignup(string username, string password) 
{
    fstream file;
    file.open("signup.txt",ios::out);
        file<<username<<endl;
        file<<password<<endl;
        file.close();
    
}
