#include<iostream>
#include<fstream>
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<windows.h>
#include<string>
using namespace std;

class employee
{
  char name[20];
  char desig[20];
  int age;
  char doj[20];
  string str;
  int salary;

  protected:
      int cpf;
      int user[8];
      char d6[4];

  public:
      void promotion()
      {
          cout<<"\n|Promote:"<<"\n|1.Salary:";
          cin>>salary;
          cout<<"\n|2.Designation:";
          cin.ignore();
          cin.getline(desig,20);
      }
      void setcpf()
     {

         cpf=1000+rand()%100;
         cout<<"\n|CPF number :"<<cpf;
     }
     void setc()
     {
         cpf=1000+rand()%100;
         cout<<endl;
     }

      void getdetails()
      {
          cout<<"\n|Enter name:";
          cin.ignore();
          cin.getline(name,20);
          cout<<"\n|Enter age:";
          cin>>age;
          if(age>60)
          {
              cout<<"\nInvalid!!!!";
              cout<<"\nEnter again:";
              getdetails();

          }
          else if(age<18)
          {
              cout<<"\n|Invalid!!";
              cout<<"\n|Enter again:";
              getdetails();
          }
          else
        {
          cout<<"\n|Enter date of joining (dd/mm/yy):";
          cin.ignore();
          cin.getline(doj,20);
          cout<<"\n|Enter designation:";
          cin.ignore();
          cin.getline(desig,20);
          cout<<"\n|Enter Salary:";
          cin>>salary;
          setcpf();
          username();
        }
      }
      void display()
      {
          cout<<"\n|Name:"<<name;
          cout<<"\n|CPF number:"<<cpf;
          cout<<"\n|Age:"<<age;
          cout<<"\n|Date of Joining:"<<doj;
          cout<<"\n|Designation:"<<desig;
          cout<<"\n|Salary:"<<salary;

      }
      int getcpf()
      {
          return cpf;
      }
      void update()
      {
          cout<<"\n|Enter Name:";
          cin.ignore();
          cin.getline(name,20);
          cout<<"\n|Enter age :";
          cin>>age;
          cout<<"\n|Enter date of joining:";
          cin.ignore();
          cin.getline(doj,20);
          /*cout<<"\n|Enter Designation:";
          cin.ignore();
          cin.getline(desig,20);*/

      }

      void getname()
      {
          cout<<name;
      }
      string retname()
      {
          str = name;
          return str;
      }
      void username()
      {
          //int yy[8];
          for(int u=0;u<8;u++)
          {
            user[u]=97 + rand()%25;
          }
       // showuser();
      }
      int* retuser()
      {
          return user;
      }
     char* nameset()
     {
         for(int d=0;d<4;d++)
         {
            d6[d]=name[d];
         }
         return d6;
     }

};

class work
{
private:
    char str[100];
protected:
    int cpf1;
public:
    void set()
     {
        cin.ignore();
        gets(str);
     }
      void put()
      {
          cin.ignore();
          puts(str);
      }
      int x;
      work()
      {
          x=0;
      }
      /*void rem()
      {
          str=void;
      }*/
};
int main()
{
     int count1=0,a1,o=0,oo=0,fy=0,setr;
     char* q;
     string pass;
     char str[100],str1[100];
     int m;
     fstream f,f1,f2,f3,f4,f5;
     f.open("data.txt",ios::out|ios::in);
     f1.open("cpf1.txt",ios::out|ios::in);
     f2.open("work.txt",ios::in|ios::out);
     f4.open("cpf.txt",ios::in|ios::out);
     f5.open("name.txt",ios::out|ios::in);
     fstream fout;
     fout.open("ongctemp.txt",ios::in|ios::out);
     int n,pwd=0,tu=0;
     employee e[10],e1[10],emp1;
     work w[5000];
     int arr[n];
     Sleep(1000);
     int s;
     int check;
     char chhh;
     char cs[2];
     char ch6[30];
     char ch1;
     cout<<"========================================================================================================================";
     cout<<"\t\t\t\t\t\tWELCOME TO O.N.G.C.!!!\n";
     cout<<"========================================================================================================================";
     Sleep(500);
     cout<<"\n\t\t\t\t\t    ---------------------------- ";
     cout<<"\n\t\t\t\t\t   |    Administrator Login:    |";
     cout<<"\n\t\t\t\t\t    ---------------------------- ";
     cout<<"\n\t\t\t\t\t     Password: ";
     char adm[6];
     for(int jg=0;jg<7;jg++)
        {
            adm[jg]=getch();
            if(jg!=6)
            cout<<"*";
        }

     int al;
     int u=0;
     if(adm[0] == '7' && adm[1]=='5' && adm[2]=='7' && adm[3]=='4' && adm[4]=='8' && adm[5]=='8')
   {
     cout<<"\n|Enter the number of employees:";
     cin>>n;
     cout<<"\n|Register Employees:\n";
       for(int i=0;i<n;i++)
         {
            e[i].getdetails();
            f.write((char*)&e[i],sizeof (e[i]));
            s=e[i].getcpf();
         }
     cout<<"\n|Registrations Done";
     Sleep(500);
     system("CLS");
     cout<<"========================================================================================================================";
     cout<<"\n\t\t\t\t\t\tWELCOME TO O.N.G.C.!!!\n";
     cout<<"========================================================================================================================";
     Sleep(500);

     do{
     cout<<"\n"<<"\n";
     cout<<"\n\t\t\t\t\t        -------------------- ";
     cout<<"\n\t\t\t\t\t       |     Login page     |";
     cout<<"\n\t\t\t\t\t        -------------------- ";
     cout<<"\n\t\t\t\t\t       |1.Administrator     |";
     cout<<"\n\t\t\t\t\t       |2.Employee          |";
     cout<<"\n\t\t\t\t\t        -------------------- ";
     int inp;
     cout<<"\n\n|Enter your choice: ";
     cin>>inp;
     if(inp==1)
    {
     system("CLS");
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t          |     WELCOME ADMINISTRATOR     |";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     //cout<<"\n\t\t\t\t           |Login:";
     cout<<"\n\t\t\t\t            PASSWORD:";
     int you[7];
     for(int j=0;j<7;j++)
     {
         you[j]=getch();
         if(j!=6)
            cout<<"*";
     }
     if(you[0] == '7' && you[1]=='5' && you[2]=='7' && you[3]=='4' && you[4]=='8' && you[5]=='8')
     {

     do
     {
     system("CLS");
     cout<<"========================================================================================================================";
     cout<<"\n\t\t\t\t\t\t\tMENU\n";
     cout<<"========================================================================================================================";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t          |   1.Details of employees:     |";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t          |   2.Work Assignment           |";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t           -------------------------------";
     cout<<"\n\t\t\t\t          |   3.Employee Schedule         |";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t          |   4.Add Employee              |";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t          |   5.Search Employee           |";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t          |   6.Remove an Employee        |";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t          |   7.Update an Employee        |";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t          |   8.Promotion                 |";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     cout<<"\n\t\t\t\t           -------------------------------";
     cout<<"\n\t\t\t\t          |   9.Server-Client Connection  |";
     cout<<"\n\t\t\t\t           ------------------------------- ";
     //cout<<"\n\n|1.Details of employees:";
     /*cout<<"\n\n|2.Work Assignment:";
     cout<<"\n\n|3.Employee Schedule:";
     cout<<"\n\n|4.Add an Employee";
     cout<<"\n\n|5.Search an employee";
     cout<<"\n\n|6.Remove an employee";
     cout<<"\n\n|7.Update an Employee";
     cout<<"\n\n|8.Promotion";
     cout<<"\n\n|9.Server-Client Connection";*/
     cout<<"\n\n|Enter your choice(1-9)";
     cin>>m;
     system("CLS");
     switch(m)
     {

         case 1  :cout<<"\n\t\t\t\t           -------------------------------";
                  cout<<"\n\t\t\t\t          |         CONTENTS ARE:         |";
                  cout<<"\n\t\t\t\t           ------------------------------- ";
                  cout<<"\n-----------------------------------------------------------------------------------------------------------------------";

                  //cout<<"\n========================================================================================================================\n";
                   //cout<<"\n|Contents are:";
                   if(n!=0)
                   {
                       for(int i=0;i<n;i++)
                      {
                          f.read((char*)&e[i],sizeof (e[i]));
                         if(e[i].getcpf()==e[i+1].getcpf() && i!=(n-1))
                          {
                               e[i].setc();
                            }
                          e[i].display();
                          Sleep(1000);
                          cout<<"\n-----------------------------------------------------------------------------------------------------------------------";
                       }
                   }
                   else
                    cout<<"\n|Empty File - Kindly add new members via option 4";
                   break;

         case 2  :cout<<"\n|NEED AUTHORISATION:";
                  cout<<"\n|PASSWORD:";
                  char aaa[6];

                 // while(pwd<6 && tu==0)
                 for(int jg=0;jg<7;jg++)
                  {
                      aaa[jg]=getch();
                      if(jg!=6)
                      cout<<"*";

                  }

                  //aaa[pwd]='\0';

                  int al;
                  if(aaa[0] == '7' && aaa[1]=='5' && aaa[2]=='7' && aaa[3]=='4' && aaa[4]=='8' && aaa[5]=='8')
                  {
                      //tu=1;
                      int jk;
                      cout<<"\n|WELCOME ADMIN";
                      cout<<"\n|Assign Duties - ";
                      cout<<"Enter employee CPF number:";
                      cin>>a1;
                      for(int ff=0;ff<n;ff++)
                      {
                        if(e[ff].getcpf()==a1)
                        jk=0;
                      }
                      if(w[a1].x!=1 && jk==0)
                    {
                      cout<<"\n|Work is not assigned";
                      for(int g=0;g<n;g++)
                      {

                          if(e[g].getcpf()==a1)
                          {

                              cout<<"\n|Assign:";
                              w[a1].set();
                              f2.write((char*)&w[a1],sizeof(w[a1]));
                              w[a1].x=1;
                              cout<<"\n|Assigning....";
                              Sleep(1000);
                              cout<<"\n|Work Alloted"<<endl;

                           }
                      }
                    }
                      //else if(f2.eof())
                      else if(w[a1].x==1)
                      {
                          cout<<"\n|Work is Assigned:";
                      }
                          //else if(e[g].getcpf()!=a1)
                          //{
                            //  cout<<"\n|Invalid CPF!!";
                          //}
                        else if(jk!=0)
                            cout<<"\n|Invalid CPF";

                      }

                 else
                    {
                    cout<<"\n| WRONG PASSWORD!!!";
                    }
                   break;





         case 3  : int d1;
                   char chh[100];
                   cout<<"\n|Login:"<<"\nCPF No:";
                   cin>>d1;
                   int d2;
                   for(int h=0;h<n;h++)
                   {
                       if(e[h].getcpf()==d1)
                       {
                           d2=0;
                           cout<<"\n|Welcome:";
                           e[h].getname();
                           cout<<"\n|Your schedule:\t";
                           f2.read((char*)&w[d1],sizeof(w[d1]));
                           w[d1].put();
                           //u=u+1;
                           /*f2.seekg(0);
                           cin.ignore();
                           f2.getline(str1,100);
                           puts(str1);
                        }*/
                       }
                   }
                   if(d2!=0)
                    cout<<"\n|Invalid CPF";


                   break;

         case 4  : cout<<"\n|Enter details:";
                   char ad[6];
                   //employee emp1[n];
                   cout<<"\n|NEED AUTHORISATION:";
                   cout<<"\n|Password:";
                   for(int jg=0;jg<7;jg++)
                  {
                      ad[jg]=getch();
                      if(jg!=6)
                      cout<<"*";
                  }

                   if(ad[0] == '7' && ad[1]=='5' && ad[2]=='7' && ad[3]=='4' && ad[4]=='8' && ad[5]=='8')
                   {
                       n=n+1;
                       e[n-1].getdetails();
                   }

                   else
                    cout<<"\n|Unauthorized";

                   break;

         case 5 : cout<<"\n|Enter CPF number:";
                   int a;
                   cin>>a;
                   for(int k =0;k<n;k++)
                   {
                       if(e[k].getcpf()==a)
                       {
                          f.read((char*)&e[k],sizeof (e[k]));
                          cout<<"\n|Please wait..";
                          Sleep(2000);
                          e[k].display();
                       }
                   }
                   break;

        case 6    : char a8[6];
                    if(n!=0)
                    {
                    cout<<"\n|NEED AUTHORISATION:";
                    cout<<"\n|PASSWORD:";
                    for(int jg=0;jg<7;jg++)
                  {
                      a8[jg]=getch();
                      if(jg!=6)
                      cout<<"*";

                  }

                    if(a8[0] == '7' && a8[1]=='5' && a8[2]=='7' && a8[3]=='4' && a8[4]=='8' && a8[5]=='8')
                   {
                    cout<<"\n|Enter CPF number: ";
                    int b;
                    cin>>b;
                    int sdf,sdf1;
                    employee emp[10];
                    for(int l=0;l<n;l++)
                    {

                        if(e[l].getcpf()==b)
                        {
                            sdf1=0;
                            cout<<"\n|Removing please wait...";
                            Sleep(2000);
                            cout<<"\n|Removed";
                            sdf=0;
                            for(int a=l;a<n;a++)
                                e[a]=e[a+1];
                            n=n-1;

                        }

                   }


                     if(sdf!=0)
                           {
                               cout<<"\n|Invalid CPF";
                           }


                    for(int uu=0;uu<n;uu++)
                        fout.write((char*)&e[uu],sizeof(e[uu]));

                   /* int cno;

                    for(int uu=0;uu<n;uu++)
                    {
                        cno=e[uu].getcpf();
                        f4<<cno<<"-";
                    }*/

                    remove("data.txt");
                    rename("ongctemp.txt", "data.txt");
                    //remove("cpf1.txt");
                    //rename("cpf.txt","cpf1.txt");
                    check=0;
                    }


                    else
                    cout<<"\n|Unauthorized: Access Denied";
                    }

                        else
                        cout<<"\n|Underflow!!!";


                break;

        case 7   : char tw[6];
                   cout<<"\n|NEED AUTHORISATION:"<<"\n|PASSWORD:";
                    for(int jg=0;jg<7;jg++)
                  {
                      tw[jg]=getch();
                      if(jg!=6)
                      cout<<"*";
                 }

                    if(tw[0] == '7' && tw[1]=='5' && tw[2]=='7' && tw[3]=='4' && tw[4]=='8' && tw[5]=='8')
                   {
                   cout<<"\n|Enter CPF Number:";
                   int d;
                   char c;
                   cin>>d;
                   for(int f=0;f<n;f++)
                   {
                       if(e[f].getcpf()==d)
                       {
                           e[f].display();
                           cout<<"\n|You wish to update : (y/n)";
                           cin>>c;
                           if(c == 'y' || c=='Y')
                           {
                               e[f].update();
                           }
                           else
                           {
                               cout<<"\n|Alright";
                               break;
                           }
                       }
                   }
                   cout<<"\n|Update Done Successfully";
                   }
                   else
                    cout<<"\n|Unauthorized";
                      break;

        case 8   : char tw2[6];
                   int sd,y1,index;
                   int y9;
                   cout<<"\n|ADMIN LOGIN"<<"\n|PASSWORD:";
                    for(int jg=0;jg<7;jg++)
                  {
                      tw2[jg]=getch();
                      if(jg!=6)
                      cout<<"*";
                  }

                    if(tw2[0] == '7' && tw2[1]=='5' && tw2[2]=='7' && tw2[3]=='4' && tw2[4]=='8' && tw2[5]=='8')
                   {
                       cout<<"\n|WELCOME ADMIN";
                       cout<<"\n|Enter the CPF number of the employee:";
                       cin>>sd;
                       for(int t=0;t<n;t++)
                       {
                           if(e[t].getcpf() == sd)
                           {
                               y9=0;
                               index = t;
                           }
                       }

                       if(y9==0)
                       {
                           e[index].promotion();
                           f.write((char*)&e[index],sizeof(e[index]));
                       }
                       else
                        {
                            cout<<"\n|Invalid CPF";
                        }
                   }
                   else
                    cout<<"\n|Unauthorized";
                    break;


        case 9   : cout<<"\n\t\t\t\t           -------------------------------";
                   cout<<"\n\t\t\t\t          |    WELCOME TO SERVER SIDE:    |";
                   cout<<"\n\t\t\t\t           ------------------------------- ";
                   cout<<"\n-----------------------------------------------------------------------------------------------------------------------";
                   //cout<<"\n|WELCOME TO SERVER SIDE:";
                   cout<<"\n|Establishing connection...";
                   Sleep(2000);
                   char cv;
                   f1.seekg(0);
                   int* fg;
                   if(n!=0)
                  {
                      //if(check!=0)
                   for(int s=0;s<n;s++)
                   {

                       f1<<e[s].getcpf()<<"-";

                   }

                   int* fh11;
                   char* fh12;
                   cout<<"\n|Connected";
                   for(int fy1=0;fy1<n;fy1++)
                   {
                     fh11=e[fy1].retuser();
                     fh12=e[fy1].nameset();
                     f5<<*fh12<<*fh11<<"-";
                     cout<<"\n|Username for ";
                     e[fy1].getname();
                     cout<<":"<<*fh12<<*fh11;

                   }
                   //f5.close();

                 /* if(check==0)
                  {

                    for(int uu=0;uu<n;uu++)
                    {
                        //cno=e[uu].getcpf();
                        f4<<e[uu].getcpf()<<"-";
                    }
                        f4.close();
                       if((remove("cpf1.txt"))!=0)
                       {
                           cout<<"\n|ERROR";
                       }
                       else cout<<"\n|Done";
                       rename("cpf.txt","cpf1.txt");

                  }*/
                   cout<<"\n|Connection Established : Kindly move to Client-Server Application";

                   /*int k9=0;
                   while(!f1.eof())
                   {
                       f1>>ch6[k9];
                        if(ch6[k9]=='-')
                       {
                           cs[0]=ch6[k9-2];
                           cs[1]=ch6[k9-1];

                       }
                       if((cs[0]==4&&cs[1]==1) || (cs[0]==6&&cs[1]==4))
                        cout<<"\n|Already registered!!";
                        k9++;
                   }*/

                  }

                  else
                  {
                      cout<<"No Employees assigned. kindly assign using option 4";
                  }


                   break;

        default  : cout<<"\n|Invalid Input!!";
                   break;
                  }


        cout<<"\n\n|Sign out?(y/n)";
        cin>>ch1;
        if(ch1 =='y' || ch1 =='Y')
        {
          cout<<"\n|Signing out...\n";
          Sleep(1000);
          cout<<"========================================================================================================================";
          cout<<"\n\t\t\t\t\t\tTHANK YOU FOR VISITING\n";
          cout<<"========================================================================================================================";
          Sleep(1000);
        }
        system("CLS");
     }while(ch1=='n' || ch1=='N');
     f.close();
     f1.close();
     f2.close();
     f3.close();
     //f4.close();
     f5.close();
     }
     else cout<<"\n|Wrong Password";
}

     if(inp==2)
   {
    system("CLS");
    cout<<"\n"<<"\n";
    cout<<"\n\t\t\t\t           ------------------------------- ";
    cout<<"\n\t\t\t\t          |        WELCOME EMPLOYEE       |";
    cout<<"\n\t\t\t\t           ------------------------------- ";
    //cout<<"\n|\t\t\t\t\t\tWELCOME EMPLOYEE ";
    //cout<<"\n\t\t\t\t           |Login:";
    cout<<"\n\t\t\t\t            Password: ";
    char adm[6];

     for(int jg=0;jg<7;jg++)
        {
            adm[jg]=getch();
            if(jg!=6)
            cout<<"*";
        }
     if(adm[0] == '7' && adm[1]=='5' && adm[2]=='7' && adm[3]=='4' && adm[4]=='8' && adm[5]=='8')
     {
           char ch;
         do
       {
         system("CLS");
         cout<<"========================================================================================================================";
         cout<<"\n\t\t\t\t\t\t\tMENU\n";
         cout<<"========================================================================================================================";
         //cout<<"\n========================================================MENU============================================================";
         cout<<"\n\n\n";
         cout<<"\n\t\t\t\t           --------------------------------- ";
         cout<<"\n\t\t\t\t          |   1.Employee Schedule           |";
         cout<<"\n\t\t\t\t           --------------------------------- ";
         //cout<<"\n|1.Employee Schedule:";
         cout<<"\n";
         cout<<"\n\t\t\t\t           --------------------------------- ";
         cout<<"\n\t\t\t\t          |   2.Server-Client connection    |";
         cout<<"\n\t\t\t\t           --------------------------------- ";
         cout<<"\n|Enter your Choice(1-2):";
         int choice;
         cin>>choice;
         system("CLS");
         switch(choice)
         {
             case 1: int d1;
                   char chh[100];
                   cout<<"\n|Login:"<<"\nCPF No:";
                   cin>>d1;
                   int d2;
                   for(int h=0;h<n;h++)
                   {
                       if(e[h].getcpf()==d1)
                       {
                           d2=0;
                           cout<<"\n|Welcome:";
                           e[h].getname();
                           cout<<"\n|Your schedule:\t";
                           f2.read((char*)&w[d1],sizeof(w[d1]));
                           w[d1].put();

                       }
                   }
                   if(d2!=0)
                    cout<<"\n|Invalid CPF";


                   break;

            case 2:cout<<"\n\t\t\t\t           -------------------------------";
                   cout<<"\n\t\t\t\t          |    WELCOME TO SERVER SIDE:    |";
                   cout<<"\n\t\t\t\t           ------------------------------- ";
                   cout<<"\n-----------------------------------------------------------------------------------------------------------------------";
                   //cout<<"\n|WELCOME TO SERVER SIDE:";
                   char cv;
                   f1.seekg(0);
                   int* fg;
                   if(n!=0)
                  { o++;
                   for(int s=0;s<n;s++)
                   {

                       f1<<e[s].getcpf()<<"-";

                   }

                   int* fh11;
                   char* fh12;
                   int cp5;
                   cout<<"\n|Enter your CPF number: ";
                   cin>>cp5;
                   cout<<"\n|Establishing connection...";
                   Sleep(2000);
                   for(int fy1=0;fy1<n;fy1++)
                   {
                    if(e[fy1].getcpf()==cp5)
                     {
                     fh11=e[fy1].retuser();
                     fh12=e[fy1].nameset();
                     //f5<<*fh12<<*fh11<<"-";
                     cout<<"\n|Username for ";
                     e[fy1].getname();
                     //f5.read((char*)&e[fy1],sizeof(e[fy1]));
                     cout<<":"<<*fh12<<*fh11;
                     }

                   }
                   cout<<"\n|Connection Established : Kindly move to Client-Server Application";


                   //int k9=0;

                  /* for(int k9=0;k9<n;k9++)
                   {

                       if(ch6[k9]=='-')
                       {
                           //char cs[2];
                           cs[0]=ch6[k9-2];
                           cs[1]=ch6[k9-1];

                       }
                       if((cs[0]==4&&cs[1]==1) || (cs[0]==6&&cs[1]==4))
                        cout<<"\n|Already registered!!";
                   }*/

                  }

                  else
                  {
                      cout<<"No Employees assigned. kindly assign using option 4";
                  }


                   break;

            default:cout<<"\n|Invalid Input!!!";
                    break;
         }
         cout<<"\n|Sign out?(y/n): ";
         cin>>ch;
         if(ch=='y')
         {
          cout<<"\n|Signing out...\n";
          Sleep(1000);
          cout<<"========================================================================================================================";
          cout<<"\n\t\t\t\t\t\tTHANK YOU FOR VISITING\n";
          cout<<"========================================================================================================================";
          Sleep(1000);
         }
         system("CLS");
         }while(ch=='n'||ch=='N');

      }
      else cout<<"\n|Wrong Password!!!";

     }
cout<<"\n|Want to continue(y/n)";
cin>>chhh;
//cout<<"\n"<<"\n"<<"\n"<<"\n"<<"\n"<<"\n"<<"\n"<<"\n";
system("CLS");
if(chhh=='y')
{
cout<<"========================================================================================================================";
cout<<"\n\t\t\t\t\t\tWELCOME TO O.N.G.C.!!!\n";
cout<<"========================================================================================================================";
Sleep(500);
}

}while(chhh=='y');
if(chhh='n')
{
 cout<<"CLOSING APPLICATION....\n";
 Sleep(1000);
 cout<<"========================================================================================================================";
 cout<<"\n\t\t\t\t\t\tTHANK YOU FOR VISITING\n";
 cout<<"========================================================================================================================";
}
}
 else
    cout<<"\n|Unauthorized!!!";

     return 0;


}


