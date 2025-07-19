#include<fstream>
using namespace std;
main()
{
    string line="Welcome to U.E.T...";
    fstream newFile;
    newFile.open("TextFile.txt",ios::out);
    newFile<<line;
    newFile.close();
}