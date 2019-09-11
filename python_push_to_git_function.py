def push(message):
    """
    Save current notebook and push whole current dir to origin/master
    
    Param:
        message : commit's message
    
    Return:
        None
    """
    assert(len(message.strip())>10)
    import subprocess
    from IPython.display import display, Javascript
    
    cmds = [  "git add .",
              "git commit -m ", 
              "git push origin master"]
    
    # save current notebook
    display(Javascript('IPython.notebook.save_checkpoint();'))
    for cmd in cmds:
        cmd = cmd.split()
        if "commit" in cmd: 
            cmd.append( f"'{message}'") 
        print(" ".join(cmd))
        subprocess.check_output(cmd)
        