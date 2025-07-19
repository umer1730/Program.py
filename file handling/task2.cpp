#include<iostream>
#include<fstream>
using namespace std;
void inputnames(string names[]);
void storenames(string names[]);
main()
{
    string names[5];
    inputnames(names);
    storenames(names);
}
void inputnames(string names[])
{
    for(int ind = 0;ind < 5;ind++)
    {
        cout<<"Enter name:";
        cin>>names[ind];
    }
}
void storenames(string names[])
{
    fstream file;
    file.open("data.txt",ios::out);
    for (int ind = 0;ind < 5;ind++)
    {
        file<<names[ind];
        file<<"\n";
    }
    file.close();
}