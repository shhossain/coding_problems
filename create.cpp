// create a project folder
#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <sstream>
#include <direct.h>
using namespace std;

// map for language extensions
map<string, string> lang_ext = {
    {"c", ".c"},
    {"cpp", ".cpp"},
    {"java", ".java"},
    {"py", ".py"},
    {"rb", ".rb"},
    {"js", ".js"},
    {"html", ".html"},
    {"css", ".css"},
    {"php", ".php"},
    {"go", ".go"},
    {"scala", ".scala"},
    {"swift", ".swift"},
    {"kotlin", ".kotlin"},
    {"rust", ".rust"},
    {"scss", ".scss"},
    {"less", ".less"},
    {"sass", ".sass"},
    {"sql", ".sql"},
    {"xml", ".xml"},
    {"json", ".json"},
    {"yaml", ".yaml"},
    {"yml", ".yml"},
    {"sh", ".sh"},
    {"bash", ".bash"},
    {"bat", ".bat"},
    {"awk", ".awk"},
    {"perl", ".perl"},
    {"pl", ".pl"},
    {"lua", ".lua"},
    {"go", ".go"},
    {"groovy", ".groovy"},
    {"scala", ".scala"},
    {"swift", ".swift"},
    {"kotlin", ".kotlin"},
    {"rust", ".rust"},
    {"scss", ".scss"},
    {"less", ".less"},
    {"sass", ".sass"},
    {"sql", ".sql"},
    {"xml", ".xml"},
    {"json", ".json"},
    {"yaml", ".yaml"},
    {"yml", ".yml"},
    {"sh", ".sh"},
    {"bash", ".bash"},
    {"bat", ".bat"},
    {"awk", ".awk"},
    {"perl", ".perl"},
    {"pl", ".pl"},
    {"lua", ".lua"},
    {"go", ".go"},
    {"groovy", ".groovy"},
    {"scala", ".scala"},
    {"swift", ".swift"},
    {"kotlin", ".kotlin"}};

// fix file name if it contains invalid characters
string safe_file_name(string file_name)
{
    string safe_file_name = "";
    for (int i = 0; i < file_name.length(); i++)
    {
        if (file_name[i] == ' ')
        {
            safe_file_name += '_';
        }
        else
        {
            safe_file_name += file_name[i];
        }
    }
    return safe_file_name;
}

void create_project(string project_name, string url = "", string language = "cpp")
{
    // if language is not in the map, throw an error
    if (lang_ext.find(language) == lang_ext.end())
    {
        cout << "Error: language not found" << endl;
        cout << "Available languages: ";
        for (auto const &x : lang_ext)
        {
            cout << x.first << " ";
        }
        return;
    }
    // create the project folder with the project name in current directory
    string project_path = "./" + project_name;
    mkdir(project_path.c_str());

    // fix project name if it has any invalid characters
    project_name = safe_file_name(project_name);

    // create file with project name
    // if language is cpp,c create main function
    string file_path = project_path + "/" + project_name + lang_ext[language];
    ofstream file(file_path);
    if (language == "cpp" || language == "c")
    {
        file << "int main(){}" << endl;
    }
    file.close();

    // create a readme file with project name and url
    string readme_name = project_path + "/README.md";
    ofstream readme(readme_name);
    readme << "## " << project_name << endl;
    // url like [Project Name](url)
    if (url != "")
    {
        readme << "* [" << project_name << "](" << url << ")" << endl;
    }
    readme.close();
}

int main()
{
    string problem_name, url, language;
    cout << "Enter Problem name: ";
    getline(cin, problem_name);

    cout << "Enter url: ";
    getline(cin, url);

    cout << "Enter language(default: cpp): ";
    getline(cin, language);

    if (problem_name == "")
    {
        cout << "Error: problem name is empty" << endl;
        return 0;
    }
    if (language == "")
    {
        language = "cpp";
    }
    create_project(problem_name, url, language);
    return 0;
}