import smtplib
from email.mime.text import MIMEText

class EmailConfig(object):

    global send_user
    global mail_host
    global password

    send_user = 'ting_lvchen@163.com'
    mail_host = 'smtp.163.com'
    password = 'LTMIWEKLVZGMTRIJSROQ'

    def send_config(self, user_lists, subject, content):
        user = "发件人昵称" + "<" + send_user + ">"
        message = MIMEText(content, _subtype="plain", _charset="utf-8")
        message['Subject'] = subject
        message['From'] = user
        message['To'] = ";".join(user_lists)

        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(send_user, password)
        server.sendmail(user, user_lists, message.as_string())
        server.close()

    def send_mail(self, pass_cases, fail_cases, not_execute_cases):
        pass_num = float(len(pass_cases))
        fail_num = float(len(fail_cases))
        not_execute_num = float(len(not_execute_cases))

        execute_num = float(pass_num + fail_num)
        total_cases = float(pass_num + fail_num + not_execute_num)
        pass_ratio = "%.2f%%" % (pass_num / total_cases * 100)
        fail_ratio = "%.2f%%" % (fail_num / total_cases * 100)

        user_lists = ['crisimple@foxmail.com']
        subject = "【邮件配置测试】"
        content = "一共 %f 个用例, 执行了 %f 个用例，未执行 %f 个用例；成功 %f 个，通过率为 %s；失败 %f 个，失败率为 %s" % (total_cases, execute_num, not_execute_num, pass_num, pass_ratio, fail_num, fail_ratio)

        self.send_config(user_lists, subject, content)


if __name__ == "__main__":
    ec = EmailConfig()
    ec.send_mail([1, 3, 5], [2, 4, 6], [1, 2, 3])