import os
import shutil
import time
import datetime

import os
import datetime

ONE_DAY_TIME = 3600*24

def delete_files_before_date(directory, days):
    # 获取当前日期
    today = datetime.date.today()
    now = time.time()

    # 计算目标日期
    target_date = today - datetime.timedelta(days=days)

    # 遍历目录下的所有文件和文件夹
    for filename in os.listdir(directory):
        dirPath = os.path.join(directory, filename)

        modification_time = os.path.getmtime(dirPath)
        
        if now - ONE_DAY_TIME > modification_time:
            if not os.path.exists(dirPath):
                continue;

            try:                   
                if os.path.isfile(dirPath):
                    os.remove(dirPath)  # 删除文件
                else:
                    shutil.rmtree(dirPath)  # 删除文件夹及其内容

                print(f"已删除文件: {dirPath}")#, {modification_date}
            except Exception:
                pass
            finally:
                print(f"Exception : {dirPath}")
                
                
        # 将最后修改时间转换为日期对象
        # modification_date = datetime.date.fromtimestamp(modification_time)

        # 判断最后修改日期是否小于目标日期
        # if modification_date < target_date:
        #     if os.path.isfile(dirPath):
        #         os.remove(dirPath)  # 删除文件
        #     else:
        #         shutil.rmtree(dirPath)  # 删除文件夹及其内容

        #     print(f"已删除文件: {dirPath}, {modification_date}")

if __name__ == "__main__":
    # 删除目录下 3天前的文件及文件夹   "D:/GameAutomator_v2.3.6",
    directory_paths = ["D:/files","D:/GameAutomator_v2.3.8/Games/ps","D:/GameAutomator_v2.3.8/Games/xbox","D:/GameAutomator_v2.3.8/Games","D:/GameAutomator_v2.3.8/AutoLog","D:/GameAutomator_v2.3.8/Snapshot/mecha","C:/Users/Administrator/AppData/Local/Temp","D:/PS5_FSROOT"] 

    # 删除多少天前的数据
    days = 2 

    for directory_path in directory_paths:
        if not os.path.exists(directory_path):
            print(f"path not exists : {directory_path}")
            continue;
           
        delete_files_before_date(directory_path, days)
    