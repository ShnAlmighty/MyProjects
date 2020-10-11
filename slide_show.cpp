#include<iostream>
using namespace std;
//#include<windows.h>

int main()
{
    cout<<"\n Enter no of pictures:";
    int n,n1;
    int t=0;
    cin>>n;

    int a[n][n][n];
    char p[n][2]; //Alignment array

    /*cout<<"\nEnter Picture Name:\n";

    for(int i=0;i<n;i++)
    {
        cin>>p[i][0];
    }*/

    cout<<"\nEnter Picture Alignment:(H/V)";
    for(int j=0;j<n;j++)
    {
        //cout<<"\nFor Pic:"<<p[j][0]<<"\tAlignment:";
        cin>>p[j][1];
    }

    for(int i=0;i<(n-1);i++)
    {
        for(int j=0;j<(n-1);j++)
        {
            if(int(p[j][1]) > int(p[j+1][1]))
            {
                char temp,temp1;
                temp=p[j][1];
                temp1=p[j][0];
                p[j][1]=p[j+1][1];
                p[j][0]=p[j+1][0];
                p[j+1][1]=temp;
                p[j+1][0]=temp1;
            }
        }
    }

   /* for(int k=0;k<n;k++)
    {
        cout<<"\nPic:"<<p[k][0]<<"\tAlignment:"<<p[k][1];
        cout<<endl;
    }*/

    /*for(int i=0;i<n;i++)
    {
        if(p[i][1] == 'v')
        {
            if(p[i+1][1]=='v')
            {
                system("CLS");
                Sleep(1000);
                cout<<"\n--------------------------------------------------------------------------------------";
                cout<<"\nSlide="<<"Pic:"<<p[i][0]<<"\t Alignment:"<<p[i][1]<<"\t\t\t\t\t\t\t      |";
                cout<<"\nSlide="<<"Pic:"<<p[i+1][0]<<"\t Alignment:"<<p[i+1][1]<<"\t\t\t\t\t\t\t      |";
                cout<<"\n--------------------------------------------------------------------------------------";
                Sleep(1000);
                i=i+1;
            }
            else
            {
                system("CLS");
                Sleep(1000);
                cout<<"\n--------------------------------------------------------------------------------------";
                cout<<"\nSlide="<<"Pic:"<<p[i][0]<<"\t Alignment:"<<p[i][1]<<"\t\t\t\t\t\t\t      |";
                cout<<"\n--------------------------------------------------------------------------------------";
                Sleep(1000);

            }
        }
        else
        {
            system("CLS");
            Sleep(1000);
                cout<<"\n--------------------------------------------------------------------------------------";
            cout<<"\nSlide="<<"Pic:"<<p[i][0]<<"\t Alignment:"<<p[i][1]<<"\t\t\t\t\t\t\t      |";
                cout<<"\n--------------------------------------------------------------------------------------";
            Sleep(1000);
        }
    }*/

    string p1[n][3][5];//main array
    int size_attributes[n];

    for(int i=0;i<n;i++)
    {
        //p1[i][0][0]=p[i][0];
        p1[i][1][0]=p[i][1];
    }

    /*for(int i=0;i<n;i++)
    {
        cout<<p1[i][0][0];
        cout<<"\t"<<p1[i][1][0];
        cout<<endl;
    }*/
    cout<<"\nEnter Attributes:\n";

    string p2[n][30]; //attributes array;

    for(int i=0;i<n;i++)
    {
        cout<<"\nEnter number of attributes:\n";
        cin>>n1;
        size_attributes[i]=n1;
        if(n1>t)
            t=n1;
        for(int k=0;k<n1;k++)
       {
         //cout<<"\nFor Pic:"<<p1[i][0][0]<<"\tAlignment:"<<p1[i][1][0]<<"\t Attributes:";
         cin>>p1[i][2][k];
         p2[i][k]=p1[i][2][k];
         cout<<endl;
       }
    }

    cout<<"\nAttributes:\n";

    /*for(int i=0;i<n;i++)
    {
        for(int j=0;j<3;j++)
        {
            cout<<p2[i][j];
        }
        cout<<endl;
    }*/


    /*for(int i=0;i<n;i++)
    {
        cout<<"\nFor Pic:"<<p1[i][0][0]<<"\tAlignment:"<<p1[i][1][0]<<"\tAttributes:<";
        for(int j=0;j<3;j++)
        {
           cout<<p1[i][2][j]<<",";
        }
        cout<<">";
    }*/

   /* for(int i=0;i<n;i++)
    {
        if(p[i][1] == 'v')
        {
            if(p[i+1][1]=='v')
            {
                system("CLS");
                Sleep(1000);
                cout<<"\n-----------------------------------------------------------";
                cout<<"\nSlide="<<"Pic:"<<p[i][0]<<"\t Alignment:"<<p[i][1]<<"\t Attributes: <"<<p1[i][2][0]<<","<<p1[i][2][1]<<","<<p1[i][2][2]<<">"<<"\t   |";
                cout<<"\nSlide="<<"Pic:"<<p[i+1][0]<<"\t Alignment:"<<p[i+1][1]<<"\t Attributes: <"<<p1[i+1][2][0]<<","<<p1[i+1][2][1]<<","<<p1[i+1][2][2]<<">"<<"\t   |";
                cout<<"\n-----------------------------------------------------------";
                Sleep(1000);
                i=i+1;
            }
            else
            {
                system("CLS");
                Sleep(1000);
                cout<<"\n-----------------------------------------------------------";
                cout<<"\nSlide="<<"Pic:"<<p[i][0]<<"\t Alignment:"<<p[i][1]<<"\t Attributes: <"<<p1[i][2][0]<<","<<p1[i][2][1]<<","<<p1[i][2][2]<<">"<<"\t   |";
                cout<<"\n-----------------------------------------------------------";
                Sleep(1000);

            }
        }
        else
        {
            system("CLS");
            Sleep(1000);
            cout<<"\n-----------------------------------------------------------";
            cout<<"\nSlide="<<"Pic:"<<p[i][0]<<"\t Alignment:"<<p[i][1]<<"\t Attributes: <"<<p1[i][2][0]<<","<<p1[i][2][1]<<","<<p1[i][2][2]<<">"<<"\t   |";
            cout<<"\n-----------------------------------------------------------";
            Sleep(1000);
        }
    }*/

  cout<<"\nChecking Proximity:\n";

    for(int i=0;i<n;i++)
    {
        int u=size_attributes[i];
        for(int j=0;j<u;j++)
        {
            for(int k=i;k<n;k++)
            {
                int u1=size_attributes[k];
                for(int m=0;m<u1;m++)
                {
                    if(p1[i][1][0] == "v")
                    {
                        if(p1[i+1][1][0]=="v")
                        {
                            if(p1[i][2][j] == p1[k+1][2][m])
                            {
                                int u2=size_attributes[k+1];
                                for(int l=0;l<u2;l++)
                                {
                                    string temp = p1[i+1][2][l];
                                    p1[i+1][2][l]=p1[k+1][2][l];
                                    p1[k+1][2][l]=temp;
                                    int temparr=size_attributes[i+1];
                                    size_attributes[i+1]=size_attributes[k+1];
                                    size_attributes[k+1]=temparr;
                                }
                            }
                        }
                        else
                        {
                            if(p1[i][2][j] == p1[k+1][2][m])
                            {
                                int u2=size_attributes[k+1];
                                for(int l=0;l<u2;l++)
                                {
                                    string temp = p1[i+1][2][l];
                                    p1[i+1][2][l]=p1[k+1][2][l];
                                    p1[k+1][2][l]=temp;
                                    int temparr=size_attributes[i+1];
                                    size_attributes[i+1]=size_attributes[k+1];
                                    size_attributes[k+1]=temparr;
                                }
                            }
                        }
                    }

                    if(p1[i][1][0] == "h")
                    {
                        if(p1[i+1][1][0]=="h")
                        {
                            if(p1[i][2][j] == p1[k+1][2][m])
                            {
                                int u2=size_attributes[k+1];
                                for(int l=0;l<u2;l++)
                                {
                                    string temp = p1[i+1][2][l];
                                    p1[i+1][2][l]=p1[k+1][2][l];
                                    p1[k+1][2][l]=temp;
                                    int temparr=size_attributes[i+1];
                                    size_attributes[i+1]=size_attributes[k+1];
                                    size_attributes[k+1]=temparr;
                                }
                            }
                        }
                        else if(p1[i+1][1][0]=="v")
                        {
                            if(p1[i][2][j] == p1[k+1][2][m])
                            {
                                int u2=size_attributes[k+1];
                                for(int l=0;l<u2;l++)
                                {
                                    string temp = p1[i+1][2][l];
                                    p1[i+1][2][l]=p1[k+1][2][l];
                                    p1[k+1][2][l]=temp;
                                    int temparr=size_attributes[i+1];
                                    size_attributes[i+1]=size_attributes[k+1];
                                    size_attributes[k+1]=temparr;
                                }
                            }
                        }
                        else if(p1[i+1][1][0]=="v")
                        {
                            if(p1[i+2][1][0]!="v")
                            {
                                if(p1[i][2][j] == p1[k+1][2][m])
                                {
                                    int u2=size_attributes[k+1];
                                    for(int l=0;l<u2;l++)
                                    {
                                        string temp = p1[i+1][2][l];
                                        p1[i+1][2][l]=p1[k+1][2][l];
                                        p1[k+1][2][l]=temp;
                                    int temparr=size_attributes[i+1];
                                    size_attributes[i+1]=size_attributes[k+1];
                                    size_attributes[k+1]=temparr;
                                    }
                                }
                            }

                        }
                    }

                }
            }
        }
    }

    /*for(int i=0;i<n;i++)
    {
        cout<<"<";
        for(int j=0;j<3;j++)
        {
            cout<<p1[i][2][j]<<",";
        }
        cout<<">\n";
    }*/

    //system("CLS");
    //Sleep(2000);
    cout<<"\nSlide Show:\n";
    //Sleep(2000);
    /*for(int i=0;i<n;i++)
    {
        if(p1[i][1][0] == "v")
        {
            if(p1[i+1][1][0]=="v")
            {
                //system("CLS");
                Sleep(1000);
                cout<<"\n--------------------------------------------------------------------------------------";
                cout<<"\nSlide="<<"Pic:"<<p[i][0]<<"\t Alignment:"<<p[i][1]<<"\t Attributes: <"<<p1[i][2][0]<<","<<p1[i][2][1]<<","<<p1[i][2][2]<<">"<<"\t\t\t      |";
                cout<<"\nSlide="<<"Pic:"<<p[i+1][0]<<"\t Alignment:"<<p[i+1][1]<<"\t Attributes: <"<<p1[i+1][2][0]<<","<<p1[i+1][2][1]<<","<<p1[i+1][2][2]<<">"<<"\t\t\t      |";
                cout<<"\n--------------------------------------------------------------------------------------";
                Sleep(1000);
                i=i+1;
            }
            else
            {
                //system("CLS");
                Sleep(1000);
                cout<<"\n--------------------------------------------------------------------------------------";
                cout<<"\nSlide="<<"Pic:"<<p[i][0]<<"\t Alignment:"<<p[i][1]<<"\t Attributes: <"<<p1[i][2][0]<<","<<p1[i][2][1]<<","<<p1[i][2][2]<<">"<<"\t\t\t      |";
                cout<<"\n--------------------------------------------------------------------------------------";
                Sleep(1000);

            }
        }
        else if(p1[i][1][0]=="h")
        {
            //system("CLS");
            Sleep(1000);
            cout<<"\n--------------------------------------------------------------------------------------";
            cout<<"\nSlide="<<"Pic:"<<p[i][0]<<"\t Alignment:"<<p[i][1]<<"\t Attributes: <"<<p1[i][2][0]<<","<<p1[i][2][1]<<","<<p1[i][2][2]<<">"<<"\t\t\t      |";
            cout<<"\n--------------------------------------------------------------------------------------";
            Sleep(1000);
            if(p1[i+1][1][0]=="v")
            {
                if(p1[i+2][1][0]!="v")
                {
                    cout<<"\n--------------------------------------------------------------------------------------";
                    cout<<"\nSlide="<<"Pic:"<<p[i+1][0]<<"\t Alignment:"<<p[i+1][1]<<"\t Attributes: <"<<p1[i+1][2][0]<<","<<p1[i+1][2][1]<<","<<p1[i+1][2][2]<<">"<<"\t\t\t      |";
                    cout<<"\n--------------------------------------------------------------------------------------";
                }
            }
        }
    }*/

    for(int i=0;i<n;i++)
    {
        cout<</*"\nPic:"<<p1[i][0][0]<<"\t*/ "Alignment:"<<p1[i][1][0]<<"\tAttributes:<";
        for(int j=0;j<size_attributes[i];j++)
        {
            cout<<p1[i][2][j]<<",";
        }
        cout<<">\n";
    }


}
