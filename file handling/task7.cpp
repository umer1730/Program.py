#include<iostream>
#include<fstream>
using namespace std;
void header() 
{
    cout << "###############################################" << endl;
    cout << "#       SIGN IN AND SIGN UP APPLICATION       #" << endl;
    cout << "###############################################" << endl;
}
void signup() 
{
    string username, password;
    cout << "=== Sign Up ===" << endl;
    cout << "Enter the username: ";
    cin >> username;
    cout << "Enter the password: ";
    cin >> password;

    fstream file;
    file.open("user.txt", ios::out);
    if (file.is_open()) {
        file << username << " " << password << endl;
        file.close();
        cout << "User registered successfully!" << endl;
    } 
    else 
    {
        cout << "Error in file opening!" << endl;
    }
}
void signin() 
{
    string username, password, fileusername, filepassword;
    bool isfound = false;
    cout << "=== Sign In ===" << endl;
    cout << "Enter username: ";
    cin >> username;
    cout << "Enter password: ";                          
    cin >> password;

    fstream file;
    file.open("user.txt", ios::in);
    if (file.is_open()) 
    {
        while (file >> fileusername >> filepassword) 
        {
            if (fileusername == username && filepassword == password) 
            {
                isfound = true;
                break;
            }
        }
        file.close();
        if (isfound) 
        {
            cout<<"Login successful! Welcome, " << username << "." << endl;
        } 
        else 
        {
            cout<<"Invalid username or password." << endl;
        }
    } 
    else 
    {
        cout << "Error in file opening!" << endl;
    }
}
int main() 
{
    header;
    int option;
    cout << "====== MENU ======" << endl;
    cout << "1. Sign up" << endl;
    cout << "2. Sign in" << endl;
    cout << "3. Exit" << endl;
    cout << "Choose any option: ";
    cin >> option;
    switch (option) {
        case 1:
            signup();
            break;
        case 2:
            signin();
            break;
        case 3:
            cout << "Exiting..." << endl;
            break;
        default:
            cout << "Invalid option. Try again." << endl;
    }
    return 0;
}