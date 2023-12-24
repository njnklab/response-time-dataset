import pandas as pd
import numpy as np
import os



df = pd.read_excel('/home/ubuntu/proj/rt-dataset/raw/新乡/excel/2021-02-27~2021-03-17.xlsx')


demographic_cols = ['export_id', '性别gender', '年龄age', '民族minzu', '教育程度edu', '你是否有吸烟史p7', '你是否有饮酒史p8']
demographic_cols_rename = ['export_id', 'gender', 'age', 'ethnicity', 'edu', 'smoke', 'drink']

phq9_cols = ['export_id', '抑郁得分t1','做事时提不起劲或没有兴趣t2','时间t2_time','感到心情失落，沮丧或绝望t3','时间t3_time',
             '入睡困难、睡不安或睡得过多t4','时间t4_time','感觉疲惫或没有活力t5','时间t5_time',
             '食欲不振或吃太多t6','时间t6_time','觉得自己很糟或觉得自己很失败，或让自己家人失望t7','时间t7_time',
             '对事物觉得专注有困难，例如看报纸或看电视时t8','时间t8_time',
             '行动或说话速度缓慢到别人已经察觉？或刚好相反--变得比平日更烦躁或坐立不安，动来动去t9','时间t9_time',
             '有不如死掉或用某种方式伤害自己的念头t10','时间t10_time']
phq9_cols_rename = ['export_id', 'score', 'question1', 'time1',
                    'question2', 'time2', 'question3', 'time3',
                    'question4', 'time4', 'question5', 'time5',
                    'question6', 'time6', 'question7', 'time7',
                    'question8', 'time8', 'question9', 'time9']

gad7_cols = ['export_id', '焦虑得分t11', '感觉紧张，焦虑或急切t12', '时间t12_time', '不能够停止或控制担忧t13', '时间t13_time',
             '对各种各样的事情担忧过多t14', '时间t14_time', 
             '很难放松下来t15', '时间t15_time', '由于不安而无法静坐t16', '时间t16_time', 
             '变得容易烦恼或急躁t17', '时间t17_time', 
             '感到似乎将有可怕的事情发生而害怕t18', '时间t18_time']
gad7_cols_rename = ['export_id', 'score', 'question1', 'time1',
                    'question2', 'time2', 'question3', 'time3',
                    'question4', 'time4', 'question5', 'time5',
                    'question6', 'time6', 'question7', 'time7']

pss_cols = ['export_id', '压力得分t19', 
            '一些无法预期的事情发生而感到心烦意乱t20', '时间t20_time',
            '感觉无法控制自己生活中重要的事情t21', '时间t21_time',
            '感到紧张不安和压力t22', '时间t22_time',
            '成功地处理恼人的生活麻烦t23', '时间t23_time',
            '感到自己是有效地处理生活中所发生的重要改变t24', '时间t24_time',
            '对于有能力处理自己私人的问题感到很有信心t25', '时间t25_time',
            '感到事情顺心如意t26', '时间t26_time',
            '发现自己无法处理所有自己必须做的事情t27', '时间t27_time',
            '有办法控制生活中恼人的事情t28', '时间t28_time',
            '常觉得自己是驾驭事情的主人t29', '时间t29_time',
            '常生气，因为很多事情的发生是超出自己所能控制的t30', '时间t30_time',
            '经常想到有些事情是自己必须完成的t31', '时间t31_time',
            '常能掌握时间安排方式t32', '时间t32_time',
            '常感到困难的事情堆积如山，而自己无法克服它们t33', '时间t33_time']
pss_cols_rename = ['export_id', 'score',
                    'question1', 'time1',
                    'question2', 'time2',
                    'question3', 'time3',
                    'question4', 'time4',
                    'question5', 'time5',
                    'question6', 'time6',
                    'question7', 'time7',
                    'question8', 'time8',
                    'question9', 'time9',
                    'question10', 'time10',
                    'question11', 'time11',
                    'question12', 'time12',
                    'question13', 'time13',
                    'question14', 'time14']

isi_cols = ['export_id', '失眠得分t34',
            '入睡困难t35', '时间t35_time',
            '难以维持睡眠t36', '时间t36_time',
            '太早就醒了的问题t37', '时间t37_time',
            '你对过去两个星期的睡眠状况满意度如何t38', '时间t38_time',
            '你认为你的睡眠问题妨碍你日常运作t39', '时间t39_time',
            '你的睡眠问题在降低生活质素而言，在其它人眼中有多明显t40', '时间t40_time',
            '你对你现时的睡眠问题有多忧虑/苦恼t41', '时间t41_time']
isi_cols_rename = ['export_id', 'score',
                    'question1', 'time1',
                    'question2', 'time2',
                    'question3', 'time3',
                    'question4', 'time4',
                    'question5', 'time5',
                    'question6', 'time6',
                    'question7', 'time7']

bss_cols = ['export_id', '自杀得分t42',
            '您希望活下去的程度如何？t43', '时间t43_time',
            '您希望死去的程度如何？t44', '时间t44_time',
            '您要活下去的理由胜过您要死去的理由吗？t45', '时间t45_time',
            '您主动尝试自杀的愿望程度如何？t46', '时间t46_time',
            '您希望外力结束自己生命，即有“被动自杀愿望”的程度如何？（如，希望一直睡下去不再醒来、意外地死去等）t47', '时间t47_time',
            '您的这种自杀想法持续存在多长时间？t48', '时间t48_time',
            '您自杀想法出现的频度如何？t49', '时间t49_time',
            '您对自杀持什么态度？t50', '时间t50_time',
            '您觉得自己控制自杀想法、不把它变成行动的能力如何？t51', '时间t51_time',
            '如果出现自杀想法，某些顾虑（如顾及家人、死亡不可逆转等）在多大程度上能阻止您自杀？t52', '时间t52_time',
            '当您想自杀时，主要是为了什么？t53', '时间t53_time',
            '您想过结束自己生命的方法了吗？t54', '时间t54_time',
            '您把自杀想法落实的条件或机会如何？t55', '时间t55_time',
            '您相信自己有能力并且有勇气去自杀吗？t56', '时间t56_time',
            '您预计某一时间您确实会尝试自杀吗？t57', '时间t57_time',
            '为了自杀，您的准备行动完成得怎样？t58', '时间t58_time',
            '您已着手写自杀遗言了吗？t59', '时间t59_time',
            '您是否因为预计要结束自己的生命而抓紧处理一些事情？如买保险或准备遗嘱。t60', '时间t60_time',
            '您是否让人知道自己的自杀想法？t61', '时间t61_time']
bss_cols_rename = ['export_id', 'score',
                    'question1', 'time1',
                    'question2', 'time2',
                    'question3', 'time3',
                    'question4', 'time4',
                    'question5', 'time5',
                    'question6', 'time6',
                    'question7', 'time7',
                    'question8', 'time8',
                    'question9', 'time9',
                    'question10', 'time10',
                    'question11', 'time11',
                    'question12', 'time12',
                    'question13', 'time13',
                    'question14', 'time14',
                    'question15', 'time15',
                    'question16', 'time16',
                    'question17', 'time17',
                    'question18', 'time18',
                    'question19', 'time19']

# rename columns
df[demographic_cols].rename(columns=dict(zip(demographic_cols, demographic_cols_rename)))    \
    .to_csv('../data/demographic.csv', index=False)
df[phq9_cols].rename(columns=dict(zip(phq9_cols, phq9_cols_rename)))    \
    .to_csv('../data/phq9.csv', index=False)
df[gad7_cols].rename(columns=dict(zip(gad7_cols, gad7_cols_rename)))    \
    .to_csv('../data/gad7.csv', index=False)
df[pss_cols].rename(columns=dict(zip(pss_cols, pss_cols_rename)))    \
    .to_csv('../data/pss.csv', index=False)
df[isi_cols].rename(columns=dict(zip(isi_cols, isi_cols_rename)))    \
    .to_csv('../data/isi.csv', index=False)
df[bss_cols].rename(columns=dict(zip(bss_cols, bss_cols_rename)))    \
    .to_csv('../data/bss.csv', index=False)

