#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

class results {
    vector<int> gradepoints, credits;
    vector<float> sem_SPI;
    int curr_sem, val, no_of_courses;
    float SPI, CPI;

public:
    void input() {
        cout << "Enter your current Sem: ";
        cin >> curr_sem;
        if (curr_sem > 8 || curr_sem<1) {
            cout << "Current Sem cannot be " <<curr_sem<<endl;
            exit(1);
        }

        for (int i = 0; i < curr_sem; i++) {
            cout<<"Enter number of courses in semester "<<(i+1)<<":";
            cin>>no_of_courses;
            cout << "Enter the credits of all the subjects for semester " << (i + 1) << " in order:" << endl;
            for (int j = 0; j < no_of_courses; j++) {
                cin >> val;
                if(val<0)
                {
                    cout<<"Credits cannot be negative";
                    exit(1);
                }
                credits.push_back(val);
            }
            cout << "Enter the gradepoints of all the subjects for semester " << (i + 1) << " in same order:" << endl;
            for (int j = 0; j < no_of_courses; j++) {
                cin >>val;
                gradepoints.push_back(val);
            }
            validGRADE(gradepoints);

            calc_SPI(gradepoints, credits);

            
            credits.clear();
            gradepoints.clear();
        }
        
        calc_CPI(sem_SPI);
    }
    void validGRADE(vector<int>&gradepoints){
        for(int i=0;i<gradepoints.size();i++){
            if(gradepoints[i]>10 || gradepoints[i]<0){
                cout<<"Invalid Grade Input, Gradepoint should be between 0 and 10"<<endl;
                exit(1);
            }
        }
    }

    void calc_SPI(vector<int>& gradepoints, vector<int>& credits) {
        float sum = 0, tot_creds = 0;
        for (int i = 0; i < credits.size(); i++) {
            sum += gradepoints[i] * credits[i];
            tot_creds += credits[i];
        }
        SPI = sum / tot_creds;
        sem_SPI.push_back(SPI);
    }

    void calc_CPI(vector<float>& sem_SPI) {
        float sum = 0;
        for (int i = 0; i < sem_SPI.size(); i++) {
            sum += sem_SPI[i];
        }
        CPI = sum / sem_SPI.size();
    }

    void display_RES() {
        for (int i = 0; i < sem_SPI.size(); i++) {
            cout << "SPI of sem " << i + 1 << ": " << sem_SPI[i] << endl;
        }
        cout << "Your CPI is: " << CPI << endl;
    }
};

int main() {
    results r;
    r.input();
    r.display_RES();
    return 0;
}
