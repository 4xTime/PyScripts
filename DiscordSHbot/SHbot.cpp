#include <cstdlib>
#include <iostream>
#include <fstream>

#ifdef _WIN32
#include <windows.h>
#else
#include <unistd.h>
#endif

void create_config_file(){
    const char* nazwa_pliku = "SHbotWebControl/config.ini";

    std::ofstream file(nazwa_pliku);
    if (file.is_open()) {
        file << "token = your_token" << std::endl;
        file << "channel_id = your_channel_id" << std::endl;
        file << "server_id = your_server_id" << std::endl;
        file.close();
        std::cout << "config file created" << std::endl;

    } else {
        std::cerr << "Error while creating a file." << std::endl;
    }
    
}

int main(){
    int ARG;
#ifdef _WIN32
    if (GetFileAttributesA("SHbotWebControl/config.ini") == INVALID_FILE_ATTRIBUTES) {
        create_config_file();
        std::cout << "You need to edit config file to make bot work" << std::endl;
        std::cout << "Add discord token" << std::endl;
        std::cout << "Add your channel_id" << std::endl;
        std::cout << "Add your server_id" << std::endl;
        std::cout<<"SHbotWebControl/config.ini"<<std::endl;
        std::cin>>ARG;
    }
    system("start cmd /c python SHbotWebControl/webSHbot.py");
    system("start cmd /c python SHbotWebControl/SiteSHbot/SHsiteBOT.py");
#else
    if (access("SHbotWebControl/config.ini", F_OK) != 0) {
         create_config_file();
        std::cout << "You need to edit config file to make bot work" << std::endl;
        std::cout << "Add discord token" << std::endl;
        std::cout << "Add your channel_id" << std::endl;
        std::cout << "Add your server_id" << std::endl;
        std::cout<<"SHbotWebControl/config.ini"<<std::endl;
        std::cin>>ARG;
    }
    system("xterm -e python SHbotWebControl/webSHbot.py &");
    system("xterm -e python SHbotWebControl/SiteSHbot/SHsiteBOT.py &");
#endif

    return 0;
}