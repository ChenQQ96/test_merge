#本地分支创建的文件
git branch —— 查看本地分支
git branch $开发分支名 —— 创建开发分支
git checkout $分支名 ——切换到分支名
git add
git commit
git push origin $开发分支 —— 提交到远程开发分支

#merge

git push —— 提交大远程主干分支
git checkout $主干分支 —— 切换到主干分支
git merge $开发分支 —— 合并开发分支到本地主干分支
    如果发生代码冲突conflict：git merge --abort —— 回滚merge操作