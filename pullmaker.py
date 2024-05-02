import os, shutil, sys
import git


def pullFolder(project, current_path, branch):
    pullPath = os.path.join(current_path + os.sep + project)
    os.chdir(pullPath.strip())
    #print(os.getcwd())
    g = git.Repo('.')
    print("Pulling %s", pullPath);
    print("Branch %s", branch);
    try:
        g.remotes.origin.pull(branch)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")

def main():
    if len(sys.argv) == 1:
        sys.exit("Please pass absolute path of project file")

    srcpath = sys.argv[1]
    
    current_path = os.path.dirname(os.path.abspath(__file__))
    with open(srcpath) as f:
        for line in f.readlines():
            branch = 'master'
            line_split = line.split()
            project_folder = line_split[0]
            if len(line_split) > 1:
                branch = line_split[1]

            pullFolder(project_folder, current_path, branch)

if __name__ == "__main__":
    main()
