import os
import datetime

path = '' #provide your dicrectory path
 
def file_despencer(path, threshold, base=True):#not to del the default path provided folder
    if os.path.isdir(path): #providing boolean if there is sub dicrectory or not
        for repo in os.listdir(path):#iterating the sub-dict in repo
            file_despencer(path + '/' + repo, threshold, False) #updating the path and calling func (recursion)
        if (not base) and len(os.listdir(path))==0:#deciding not to delete base dict but sub dict
            os.rmdir(path) #removing empty directory
        return


    mod_time = os.path.getmtime(path)
    #modifified time of files or folder
    if thres > mod_time:
        os.remove(path)  #removing file which meets block's conditon

threshold = (datetime.datetime.now() - datetime.timedelta(minutes=1)).timestamp()
#datetime.now() get present time 
#timedelta ---> used for calculating differences in dates and times
#timestamp() --> return the date and time of the day, accurate to a small fraction of a second

file_despencer(path,threshold) #calling the function

