#include<iostream>
#include<fstream>
using namespace std;
void read_rec(string &name, int &admissionnumber, float &percentage);
void write_rec(string name, int admissionnumber, float percentage);
int main() 
{
    string name;
    int admissionnumber;
    float percentage;  
    read_rec(name, admissionnumber, percentage);
    write_rec(name, admissionnumber, percentage);
    return 0;
}
void read_rec(string &name, int &admissionnumber, float &percentage) 
{
    cout<< "Enter the name: ";
    cin >> name;
    cout<<"Enter the admission number: ";
    cin>>admissionnumber;
    cout<< "Enter the percentage: ";
    cin>> percentage;
    fstream file;
    file.open("student.txt", ios::out);
    if (file.is_open()) 
    {
        file << name << " " << admissionnumber << " " << percentage;
        file.close();
    } 
    else 
    {
        cout << "Error opening file for writing!\n";
    }
}
void write_rec(string name, int admissionnumber, float percentage) 
{
    if (percentage > 75) 
    {
        fstream file;
        file.open("topperstudents.txt", ios::app); 
        if (file.is_open()) 
        {
            file << name << " " << admissionnumber << " " << percentage << endl;
            file.close();
        } 
        else 
        {
            cout << "Error opening file for writing!\n";
        }
    }
}