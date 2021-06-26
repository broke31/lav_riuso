


def reformat_ant(df_ant):
    df_ant['Release'] = df_ant['Release'].replace(['ant-1.1'], 'Ant1.1')
    df_ant['Release'] = df_ant['Release'].replace(['ant-1.2'], 'Ant1.2')
    df_ant['Release'] = df_ant['Release'].replace(['ant-1.3'], 'Ant1.3')
    df_ant['Release'] = df_ant['Release'].replace(['ant-1.4'], 'Ant1.4')
    df_ant['Release'] = df_ant['Release'].replace(['ant-1.5'], 'Ant1.5')
    df_ant['Release'] = df_ant['Release'].replace(['ant-1.6.0'], 'Ant1.6')


    df_ant['Release'] = df_ant['Release'].replace(['ant-1.7.0'], 'Ant1.7')

    df_ant["Class Name"] = df_ant["Class Name"].str.replace(".java", "")
    return df_ant

#def reformatted_junit(df_junit):
    #    df_junit['Release'] = df_junit['Release'].replace(["junit-3.4"],"JUnit3.4")
    # df_junit['Release'] = df_junit['Release'].replace(["junit-3.7"],"JUnit3.7")
    ##df_junit['Release'] = df_junit['Release'].replace(["junit-4.0"],"JUnit4.0")
    #df_junit['Release'] = df_junit['Release'].replace(["junit-4.2"],"JUnit4.2")
    #df_junit['Release'] = df_junit['Release'].replace(["junit-4.6"],"JUnit4.6")
    ##df_junit['Release'] = df_junit['Release'].replace(["junit-4.7"],"JUnit4.7")
    #df_junit["Class Name"] = df_junit["Class Name"].str.replace(".java", "")
    #return df_junit


def reformatted_jedit(df_jedit):
    df_jedit['Release'] = df_jedit['Release'].str.replace("source","")
    df_jedit['Release'] = df_jedit['Release'].replace(["jedit321"],"Jedit3.2.1")
    df_jedit['Release'] = df_jedit['Release'].replace(["jedit40"],"Jedit4.0")
    df_jedit['Release'] = df_jedit['Release'].replace(["jedit41"],"Jedit4.1")
    df_jedit['Release'] = df_jedit['Release'].replace(["jedit42"],"Jedit4.2")
    df_jedit['Release'] = df_jedit['Release'].replace(["jedit4.3"],"Jedit4.3")
    df_jedit["Class Name"] = df_jedit["Class Name"].str.replace(".java", "")
    return df_jedit


def reformatted_jhotdraw(df_jhotdraw):
    df_jhotdraw['Release'] = df_jhotdraw['Release'].replace(["JHotDraw5.2"],"JHotDraw52")
    df_jhotdraw['Release'] = df_jhotdraw['Release'].replace(["JHotDraw_5_3"],"JHotDraw53")
    df_jhotdraw['Release'] = df_jhotdraw['Release'].replace(["jhotdraw60b1"],"JHotDraw60")

    df_jhotdraw["Class Name"] = df_jhotdraw["Class Name"].str.replace(".java", "")
    return df_jhotdraw



def reformatted_junit(df_junit):
    df_junit['Release'] = df_junit['Release'].replace(["junit-3.4"], "JUnit3.4")
    df_junit['Release'] = df_junit['Release'].replace(["junit-3.7"], "JUnit3.7")
    df_junit['Release'] = df_junit['Release'].replace(["junit-4.0"], "JUnit4.0")
    df_junit['Release'] = df_junit['Release'].replace(["junit-4.2"], "JUnit4.2")
    df_junit['Release'] = df_junit['Release'].replace(["junit-4.6"], "JUnit4.6")
    df_junit['Release'] = df_junit['Release'].replace(["junit-4.7"], "JUnit4.7")
    df_junit["Class Name"] = df_junit["Class Name"].str.replace(".java", "")
    return df_junit
