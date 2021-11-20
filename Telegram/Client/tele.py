""""
Mr.Kataei 8/4/2021
for telebot library need token which father bot make for us , for now we define it ,
in static variable in future define and use in environment linux

this file have 2 class for store users already use bot 1-User , 2-Register
*User for all users that already sign up to system we store their chat_id and name and session
(session shows us user login or not)
*Register for all new users we store chat_id and username and 2 password and
security question and question id and answer for insert to database after insert the object remove for
avoid memory leak ,
"""
from time import sleep

from telebot import types
from telebot import apihelper
from Auth.register import register
from Inc import functions
from Account.clients import User
from Libraries.definitions import *
from Interfaces.telegram import Telegram

apihelper.ENABLE_MIDDLEWARE = True

# @testkourosh2bot -> address // use this bot for test your code
API_KEY = '1978536410:AAE_RMk3-4r_cLnt_nRcEnZHaSp-vIk9oVo'


class ClientBot(Telegram):
    def __init__(self):
        Telegram.__init__(self, API_KEY=API_KEY)

    def plan_keyboard(self, message):
        key_markup = types.ReplyKeyboardMarkup(row_width=3)
        plans = functions.get_plans()
        plan_description = ""
        for plan in plans:
            plan_row = functions.record_dictionary(record=plan, table='plans')
            key_markup.add(types.KeyboardButton(plan_row['plan']))
            plan_description += 'plan name : ' + plan_row['plan'] + '\ndescription : ' + plan_row['description'] + \
                                '\ncost : ' + str(plan_row['cost']) + '\nduration: ' + str(plan_row['duration']) + \
                                ' days\n\n'
        self.bot.send_message(message.chat.id, plan_description, reply_markup=key_markup)

    def check_is_valid_user(self, message):
        result = functions.check_expire_plan(chat_id=message.chat.id)
        if result:
            self.bot.send_message(message.chat.id, 'your plan  is expire!\n'
                                                   'recharge your plan please.')
            return False
        else:
            return True

    def bot_actions(self):
        @self.bot.message_handler(commands=['start'])
        def welcome(message):
            user = functions.get_user(message.chat.id)
            self.bot.send_chat_action(chat_id=message.chat.id, action="typing")
            sleep(1)
            self.bot.reply_to(message, trans('C_hello') + message.chat.first_name + "!\n" + trans('C_welcome'))
            if message.chat.id not in self.user_dict:
                self.user_dict[message.chat.id] = User(chat_id=message.chat.id)  # create object for register user
            if not user:
                keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
                reg_button = types.KeyboardButton(text="Share your phone number", request_contact=True)
                keyboard.add(reg_button)
                self.bot.send_message(message.chat.id,
                                      "You should share your phone number",
                                      reply_markup=keyboard)
            else:
                if self.check_is_valid_user(message=message):
                    self.bot.send_message(message.chat.id, 'Welcome back')
                    # if user deleted telegram account need develop

        @self.bot.message_handler(content_types=['contact'])
        def register_handler(message):
            user = self.user_dict[message.chat.id]
            user.number = message.contact.phone_number
            markup = types.ReplyKeyboardRemove(selective=False)
            self.bot.send_message(message.chat.id, 'please enter your username', reply_markup=markup)
            self.bot.register_next_step_handler(message, callback=reg_step_1)

        def reg_step_1(message):
            user = self.user_dict[message.chat.id]
            try:
                if functions.check_username_exist(username=message.text):
                    self.bot.send_message(message.chat.id, 'username already exist!\nTry again!')
                    self.bot.register_next_step_handler(message, reg_step_1)
                else:
                    user.username = message.text
                    error, detail = register(username=user.username, chat_id=user.chat_id, phone=user.number)
                    if error:
                        self.bot.reply_to(message, trans('C_please_start'))
                    else:
                        functions.update_user_online(username=user.username, online=True)
                        self.bot.reply_to(message, 'Welcome!\n'
                                                   'your account created!\n'
                                                   'free plan is available for 30 day\n'
                                                   'enjoy!')
            except Exception as e:
                self.bot.reply_to(message, trans('C_please_start'))
                print(e)

        @self.bot.message_handler(commands=['help'], func=self.check_is_valid_user)
        def help_me(message):
            try:
                self.bot.reply_to(message, trans('C_help'))

            except Exception as e:
                self.bot.reply_to(message, trans('C_unsuccessful_operation'))
                print(e)

        @self.bot.message_handler(commands=['guide'])
        def guide_me(message):
            try:
                self.bot.reply_to(message, trans('C_guide'))

            except Exception as e:
                self.bot.reply_to(message, trans('C_unsuccessful_operation'))
                print(e)

# def bot_actions(self):
# def bot_actions(self):
#     @self.bot.middleware_handler(update_types=['message'])
#     def activate_language(bot_instance, message):
#         activate(message.from_user.language_code)
#
#     # def command_interface_words(message):
#     #     request = message.text.split()
#     #     commands_emoji = ['➕', '🤔', '🆕', '📊', '🕯', '📺', '🧐', '❌', '🙏🏽', '⏱', '👋🏽']
#     #     if len(request) <= 2 or request[0] not in commands_emoji:
#     #         return False
#     #     else:
#     #         return True
#     #
#     # @self.bot.message_handler(func=command_interface_words)
#     # def command_message_handler(message):
#     #     if message.text == trans('C_add_keyboard'):
#     #         add_coin(message)
#     #     elif message.text == trans('C_new_keyboard'):
#     #         new_watchlist(message)
#     #     elif message.text == trans('C_analysis_keyboard'):
#     #         set_analysis(message)
#     #     # elif message.text == trans('C_candle_keyboard'):
#     #     #     show_candle(message)
#     #     elif message.text == trans('C_show_keyboard'):
#     #         show_details(message)
#     #     # elif message.text == trans('C_recommendation_keyboard'):
#     #     #     show_recommendation(message)
#     #     elif message.text == trans('C_remove_keyboard'):
#     #         remove(message)
#     #     elif message.text == trans('C_help_keyboard'):
#     #         help_me(message)
#     #     elif message.text == trans('C_frame_keyboard'):
#     #         update_timeframe(message)
#     #     elif message.text == trans('C_last_keyboard'):
#     #         get_last_recommendation(message)
#     #     elif message.text == trans('C_logout_keyboard'):
#     #         logout(message)
#
#     @self.bot.message_handler(commands=['start'])
#     def welcome(message):
#         if message.chat.id not in self.user_dict:
#             self.user_dict[message.chat.id] = User()
#         if not self.check_login(message):
#             self.bot.send_chat_action(chat_id=message.chat.id, action="typing")
#             sleep(1)
#             self.user_dict[message.chat.id].session = True
#             self.bot.reply_to(message, trans('C_hello') + message.chat.first_name + "!\n" + trans('C_welcome'))
#             step_kb = telebot.types.InlineKeyboardMarkup(row_width=2)
#             step_kb.row(telebot.types.InlineKeyboardButton(trans('C_login'), callback_data='login'),
#                         telebot.types.InlineKeyboardButton(trans('C_register'), callback_data='reg'))
#             step_kb.row(telebot.types.InlineKeyboardButton(trans('C_login_chat_id'), callback_data='login_chat_id'))
#             step_kb.row(telebot.types.InlineKeyboardButton(trans('C_forget_password'), callback_data='forget'))
#             self.bot.send_message(chat_id=message.chat.id, text=trans('C_any_account'), reply_markup=step_kb)
#
#     # after callback @bot.callback_query_handler get function parameter ,this always true
#     # and w8 to one case login and reg and .. happened . need to develop func in parameter
#     @self.bot.callback_query_handler(func=lambda call: True)
#     def query_handler(call):
#         if call.data == "login":
#             self.bot.reply_to(call.message, trans('C_enter_username'))
#             # handle next step message user enter after login
#             self.bot.register_next_step_handler(call.message, callback=self.process_login_username)
#         elif call.data == "login_chat_id":
#             self.easy_login(message=call.message)
#         elif call.data == "reg":
#             user = functions.get_user(call.message.chat.id)
#             if not user:
#                 # create object from user and store in our dictionary with chat_id key value
#                 if call.message.chat.id not in self.reg_dict:
#                     user = Register(call.message.chat.id)
#                     self.reg_dict[call.message.chat.id] = user
#                 self.bot.reply_to(call.message, trans('C_enter_username'))
#                 # handle next step message user enter after sign up
#                 self.bot.register_next_step_handler(call.message, callback=process_reg_step_1)
#             else:
#                 username = user[0][0]  # username
#                 self.bot.reply_to(call.message,
#                                   trans('C_already_have_account') + f" {username} \n" + trans('C_please_start'))
#                 self.user_dict[call.message.chat.id].session = False
#         elif "security_question_" in call.data:
#             # in other keyboard we need calls back from user choose which one question
#             security_question = str(call.data).split('_')
#             user = self.reg_dict[call.message.chat.id]
#             # store in our object
#             user.security_question_id = int(security_question[2])
#             self.bot.reply_to(call.message, trans('C_enter_answer'))
#             # handle next step message user enter after choose question
#             self.bot.register_next_step_handler(call.message, callback=process_reg_step_4)
#         elif call.data == "forget":
#             # create object from user and store in our dictionary with chat_id key value
#             user = Register(call.message.chat.id)
#             self.reg_dict[call.message.chat.id] = user
#             self.bot.reply_to(call.message, trans('C_enter_username'))
#             # handle next step message user enter after forget password
#             self.bot.register_next_step_handler(call.message, callback=process_forget_step_1)
#         # elif call.data == "watchlist":
#         #
#         #     coins = []
#         #     for index, coin in self.coins_list:
#         #         coins.append(telebot.types.InlineKeyboardButton(coin, callback_data=coin))
#         #     final = []
#         #     for i in range(0, len(coins) - 2, 3):
#         #         row = []
#         #         for j in range(i, i + 3):
#         #             row.append(coins[j])
#         #         final.append(row)
#         #     del coins
#         #     coin_keyboard = telebot.types.InlineKeyboardMarkup(final)
#         #     self.bot.send_message(chat_id=call.message.chat.id, text=trans('C_select_coin'),
#         #                           reply_markup=coin_keyboard)
#         #
#         # # need more develop
#         # elif call.data in self.coins_list[:, 1]:
#         #     coin = self.coins_list[np.where(self.coins_list[:, 1] == call.data)][0][0]
#         #     # for coins in coins[:1]:
#         #     user = self.user_dict[call.message.chat.id]
#         #     if not functions.set_coin(user.username, coin, user.watchlist[0][2])[0]:
#         #         self.bot.reply_to(call.message, trans('C_coin_already_exist'))
#         #     else:
#         #         self.bot.reply_to(call.message, trans('C_done') + "\n"
#         #                           + trans('C_default_timeframe') + "\n" + trans('C_change_timeframe'))
#         #
#         # elif call.data in self.timeframes_list[:, 1]:
#         #     time_id = self.timeframes_list[np.where(self.timeframes_list[:, 1] == call.data)][0][0]
#         #     time = self.timeframes_list[np.where(self.timeframes_list[:, 1] == call.data)][0][1]
#         #     # for coins in coins[:1]:
#         #     user = self.user_dict[call.message.chat.id]
#         #     functions.update_timeframe(user.username, time_id)
#         #     self.bot.reply_to(call.message, trans('C_done') + trans('C_timeframe_changed') + time)
#         #
#         # elif call.data in self.analysis_list[:, 1]:
#         #     user = self.user_dict[call.message.chat.id]
#         #     analysis_id = self.analysis_list[np.where(self.analysis_list[:, 1] == call.data)][0][0]
#         #     functions.set_user_analysis(user.username, int(analysis_id))
#         #     description = functions.get_description_analysis(int(analysis_id))
#         #     self.bot.reply_to(call.message,
#         #                       trans('C_done') + "\n" + trans('C_now') + call.data + trans('C_working_for_you')
#         #                       + "\n" + "description:\n" + description)
#         # elif call.data == "remove_watchlist":
#         #     user = self.user_dict[call.message.chat.id]
#         #     user.watchlist = functions.get_user_watchlist(user.username)
#         #     if user.watchlist:
#         #         watchlist_remove = telebot.types.InlineKeyboardMarkup()
#         #         # for watch in user.watchlist :
#         #         user.temp_watch = user.watchlist[0][2]
#         #         watchlist_remove.add(
#         #             telebot.types.InlineKeyboardButton(user.watchlist[0][2],
#         #                                                callback_data='watchlist_remove_step2'))
#         #         self.bot.send_message(chat_id=call.message.chat.id, text=trans('C_select_watchlist'),
#         #                               reply_markup=watchlist_remove)
#         #     else:
#         #         self.bot.reply_to(call.message, trans('C_null_watchlist'))
#         # elif call.data == "watchlist_remove_step2":
#         #     user = self.user_dict[call.message.chat.id]
#         #     functions.delete_watchlist(user.username, user.temp_watch)
#         #     self.bot.reply_to(call.message, trans('C_done') + '\n' + trans('C_create_watchlist'))
#         #
#         # elif call.data == "remove_coins":
#         #     user = self.user_dict[call.message.chat.id]
#         #     user.watchlist = functions.get_user_watchlist(user.username)
#         #     if user.watchlist:
#         #         if functions.get_empty_coins_remain(user.username, user.watchlist[0][2]) == 2:
#         #             self.bot.reply_to(call.message, trans('C_null_coin'))
#         #         else:
#         #             watchlist_remove = telebot.types.InlineKeyboardMarkup()
#         #             # for watch in user.watchlist :
#         #             user.temp_watch = user.watchlist[0][2]
#         #             watchlist_remove.add(telebot.types.InlineKeyboardButton(user.watchlist[0][2],
#         #                                                                     callback_data='coins_remove_step2'))
#         #             self.bot.send_message(chat_id=call.message.chat.id, text=trans('C_select_watchlist'),
#         #                                   reply_markup=watchlist_remove)
#         #     else:
#         #         self.bot.reply_to(call.message,
#         #                           trans('C_create_watchlist_first') + '\n' + trans('C_create_watchlist'))
#         # elif call.data == "coins_remove_step2":
#         #     user = self.user_dict[call.message.chat.id]
#         #     user.watchlist = functions.get_user_watchlist(user.username)
#         #     coin_keyboard = telebot.types.InlineKeyboardMarkup()
#         #     user_coins = functions.get_user_coins(user.username, user.watchlist[0][2])
#         #     for coin in user_coins:
#         #         coin_keyboard.add(telebot.types.InlineKeyboardButton(coin, callback_data=coin + " delete_coin"))
#         #     self.bot.send_message(chat_id=call.message.chat.id, text=trans('C_select_coin'),
#         #                           reply_markup=coin_keyboard)
#         #
#         # elif "delete_coin" in call.data:
#         #     user = self.user_dict[call.message.chat.id]
#         #     temp = str(call.data).split(" ")
#         #     coin = self.coins_list[np.where(self.coins_list[:, 1] == temp[0])][0][0]
#         #     functions.set_null_coin_user(user.username, coin)
#         #     self.bot.reply_to(call.message, trans('C_done') + '\n' + trans('C_add_coins'))
#         #
#         # elif "remove_analysis" in call.data:
#         #     user = self.user_dict[call.message.chat.id]
#         #     analysis_keyboard = telebot.types.InlineKeyboardMarkup()
#         #     analysis = functions.get_user_analysis(user.username)
#         #     if analysis:
#         #         for anal in analysis:
#         #             analysis_keyboard.add(telebot.types.InlineKeyboardButton(functions.get_analysis(anal[2])[0][0],
#         #                                                                      callback_data="analysis_delete_" +
#         #                                                                                    str(anal[2])))
#         #         self.bot.send_message(chat_id=call.message.chat.id, text=trans('C_select_analysis'),
#         #                               reply_markup=analysis_keyboard)
#         #     else:
#         #         self.bot.reply_to(call.message, trans('C_set_analysis_first'))
#         #
#         # elif "analysis_delete_" in call.data:
#         #     user = self.user_dict[call.message.chat.id]
#         #     temp = str(call.data).split('_')
#         #     functions.delete_analysis(username=user.username, analysis_id=int(temp[2]))
#         #     self.bot.send_message(chat_id=call.message.chat.id, text=trans('C_done'))
#         #
#         # elif '_tradingview_' in call.data:
#         #     user = self.user_dict[call.message.chat.id]
#         #     data = str(call.data).split('_')
#         #     option = data[2]
#         #     recom = tr(data[0], user.timeframe, option)[0]
#         #     indicators = ''
#         #     for compute in recom['COMPUTE']:
#         #         indicators += compute + ':' + recom['COMPUTE'][compute] + ',    '
#         #     result = f'{data[0]}\n' \
#         #              f'{trans("C_recommendation")} : {recom["RECOMMENDATION"]} \n' \
#         #              f'{trans("C_buy")} : {recom["BUY"]} \n' \
#         #              f'{trans("C_sell")} : {recom["SELL"]} \n' \
#         #              f'{trans("C_neutral")} : {recom["NEUTRAL"]}\n' \
#         #              f'{trans("C_Compute")} :\n{indicators}'
#         #     self.bot.reply_to(call.message, result)
#
#         # after call back done keyboard delete
#         self.bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
#
#     """
#         register handler
#     """
#
#     def process_reg_step_1(message):
#         try:
#             # fetch object
#             user = self.reg_dict[message.chat.id]
#             user.username = message.text
#             msg = self.bot.reply_to(message, '👮🏻‍♂' + trans('C_enter_password') + trans('C_password_instruction'))
#             self.bot.register_next_step_handler(msg, process_reg_step_2)
#         except Exception as e:
#             self.bot.reply_to(message, trans('C_please_start'))
#             self.user_dict[message.chat.id].session = False
#             print(e)
#
#     def process_reg_step_2(message):
#         try:
#             user = self.reg_dict[message.chat.id]
#             user.password1 = message.text
#             msg = self.bot.reply_to(message, trans('C_enter_password') + trans('C_again'))
#             self.bot.register_next_step_handler(msg, process_reg_step_3)
#             # delete password for privacy
#             self.bot.delete_message(message.chat.id, message.message_id)
#         except Exception as e:
#             self.bot.reply_to(message, trans('C_please_start'))
#             self.user_dict[message.chat.id].session = False
#             print(e)
#
#     def process_reg_step_3(message):
#         try:
#             user = self.reg_dict[message.chat.id]
#             user.password2 = message.text
#             question_dict = functions.get_security_questions()
#             self.bot.delete_message(message.chat.id, message.message_id)
#             # select question
#             questions = telebot.types.InlineKeyboardMarkup()
#             questions.add(telebot.types.InlineKeyboardButton(question_dict[0][1],
#                                                              callback_data="security_question_1"))
#             questions.add(telebot.types.InlineKeyboardButton(question_dict[1][1],
#                                                              callback_data="security_question_2"))
#             self.bot.send_message(chat_id=message.chat.id, text='⚠️' + trans('C_select_security_question'),
#                                   reply_markup=questions)
#         except Exception as e:
#             self.bot.reply_to(message, trans('C_please_start'))
#             self.user_dict[message.chat.id].session = False
#             print(e)
#
#     def process_reg_step_4(message):
#         try:
#             user = self.reg_dict[message.chat.id]
#             user.answer = message.text
#             # insert to database
#             result, error = register.register(username=user.username, chat_id=user.chat_id, password=user.password1,
#                                               password2=user.password2, question_id=user.security_question_id,
#                                               answer=user.answer)
#             self.bot.reply_to(message, error + "\n" + trans('C_please_start'))
#             self.user_dict[message.chat.id].session = False
#             self.bot.delete_message(message.chat.id, message.message_id)
#             del self.reg_dict[message.chat.id]
#         except Exception as e:
#             self.bot.reply_to(message, trans('C_please_start'))
#             self.user_dict[message.chat.id].session = False
#             print(e)
#
#     """
#         forget message  handler
#     """
#
#     def process_forget_step_1(message):
#         try:
#             user = self.reg_dict[message.chat.id]
#             user.username = message.text
#             # check user exists if dont handle this next step crashed ->get_user_security_id handled this
#             q_id = functions.get_user_security_id(user.username)
#             question = functions.get_security_questions(q_id)
#             if q_id:
#                 user.security_question_id = q_id
#                 user.security_question = functions.get_security_questions(q_id)
#                 msg = self.bot.reply_to(message, question[0][1])
#                 self.bot.register_next_step_handler(msg, process_forget_step_2)
#             else:
#                 self.bot.send_message(chat_id=message.chat.id,
#                                       text=trans('C_username_exist') + '\n' + trans('C_please_start'))
#                 self.user_dict[message.chat.id].session = False
#                 del self.reg_dict[message.chat.id]
#
#         except Exception as e:
#             self.bot.reply_to(message, trans('C_please_start'))
#             self.user_dict[message.chat.id].session = False
#             print(e)
#
#     def process_forget_step_2(message):
#         try:
#             user = self.reg_dict[message.chat.id]
#             user.answer = message.text
#             msg = self.bot.reply_to(message, trans('C_new_password'))
#             self.bot.register_next_step_handler(msg, process_forget_step_3)
#         except Exception as e:
#             self.bot.reply_to(message, trans('C_please_start'))
#             self.user_dict[message.chat.id].session = False
#             print(e)
#
#     def process_forget_step_3(message):
#         try:
#             user = self.reg_dict[message.chat.id]
#             user.password1 = message.text
#             msg = self.bot.reply_to(message, trans('C_enter_password') + trans('C_again'))
#             self.bot.delete_message(message.chat.id, message.message_id)
#             self.bot.register_next_step_handler(msg, process_forget_step_4)
#         except Exception as e:
#             self.bot.reply_to(message, trans('C_please_start'))
#             self.user_dict[message.chat.id].session = False
#             print(e)
#
#     def process_forget_step_4(message):
#         try:
#             user = self.reg_dict[message.chat.id]
#             user.password2 = message.text
#             # reset_password function handle all error about passwords and wrong answer
#             res = reset_password.reset_password(username=user.username, answer=user.answer,
#                                                 new_password=user.password1, new_password2=user.password2)
#             self.bot.reply_to(message, res)
#             self.bot.delete_message(message.chat.id, message.message_id)
#             # after reset password and update database we dont need this object
#             self.user_dict[message.chat.id].session = False
#             del self.reg_dict[message.chat.id]
#         except Exception as e:
#             self.bot.reply_to(message, trans('C_please_start'))
#             self.user_dict[message.chat.id].session = False
#             print(e)
#
#     # """
#     #     new command handler / for new watchlist
#     # """
#     #
#     # @self.bot.message_handler(commands=['new'])
#     # def new_watchlist(message):
#     #     if self.check_login(message):
#     #         user = self.user_dict[message.chat.id]
#     #         if not functions.get_user_watchlist(user.username):
#     #             self.bot.reply_to(message, trans('C_enter_watchlist_name'))
#     #             self.bot.register_next_step_handler(message, process_new_watch)
#     #         else:
#     #             self.bot.reply_to(message, trans('C_already_have_watchlist'))
#     #
#     # def process_new_watch(message):
#     #     try:
#     #         # fetch object
#     #         user = self.user_dict[message.chat.id]
#     #         for create in range(0, 4):
#     #             functions.create_watchlist(user.username, message.text)
#     #         user.watchlist = message.text
#     #         self.bot.reply_to(message, trans('C_good') + "\n" + trans('C_add_coins'))
#     #     except Exception as e:
#     #         self.bot.reply_to(message, trans('C_please_start'))
#     #         print(e)
#     #
#     # @self.bot.message_handler(commands=['add'])
#     # def add_coin(message):
#     #     if self.check_login(message):
#     #         user = self.user_dict[message.chat.id]
#     #         user.watchlist = functions.get_user_watchlist(user.username)
#     #         if user.watchlist:
#     #             if functions.get_empty_coins_remain(user.username, user.watchlist[0][2]) != 0:
#     #                 watchlist = telebot.types.InlineKeyboardMarkup()
#     #                 watchlist.add(telebot.types.InlineKeyboardButton(user.watchlist[0][2],
#     #                                                                  callback_data='watchlist'))
#     #                 self.bot.send_message(chat_id=message.chat.id, text=trans('C_select_watchlist'),
#     #                                       reply_markup=watchlist)
#     #             else:
#     #                 self.bot.reply_to(message, trans('C_full_watchlist'))
#     #         else:
#     #             self.bot.reply_to(message, trans('C_create_watchlist_first'))
#
#     """
#         get last recommendation
#     """
#
#     @self.bot.message_handler(commands=['last'])
#     def get_last_recommendation(message):
#         if self.check_login(message):
#             user = self.user_dict[message.chat.id]
#             watchlists = functions.get_user_watchlist(user.username)
#             user_analysis = functions.get_user_analysis(user.username)[0][2]
#             analysis_name = functions.get_analysis(user_analysis)[0][0]
#             signals = ""
#             if watchlists:
#                 for watchlist in watchlists:
#                     if watchlist[1]:
#                         coin = functions.get_coin_name(watchlist[1])
#                         recom = functions.get_recommendations(analysis_id=user_analysis, coin_id=watchlist[1])
#                         if recom:
#                             recom = recom[0]
#                             timeframe = functions.get_timeframe(recom[5])[0][0]
#                             risk = recom[7]
#                             position = recom[2]
#                             current_price = recom[4]
#                             target_price = recom[3]
#                             signals += f'💥*{analysis_name}*!!!\n' \
#                                        f'*{coin}* {trans("M_in")} *{position}* {trans("M_position")}\n' \
#                                        f'{trans("M_current_price")}: {current_price}$\n' \
#                                        f'{trans("M_target_price")}: {target_price}$\n' \
#                                        f'{trans("M_risk")}: *{risk}*\n' \
#                                        f'{trans("C_timeframe")}: {timeframe}\n\n'
#             self.bot.send_message(chat_id=message.chat.id, text=signals, parse_mode='Markdown')
#
#     """
#         timeframe command handler update
#     """
#
#     @self.bot.message_handler(commands=['frame'])
#     def update_timeframe(message):
#         if self.check_login(message):
#             time_keyboard = telebot.types.InlineKeyboardMarkup()
#             for index, time in self.timeframes_list:
#                 time_keyboard.add(telebot.types.InlineKeyboardButton(time, callback_data=time))
#             self.bot.send_message(chat_id=message.chat.id, text=trans('C_select_timeframe'),
#                                   reply_markup=time_keyboard)
#
#     """
#         show command handler
#     """
#
#     # @self.bot.message_handler(commands=['show'])
#     # def show_details(message):
#     #     if self.check_login(message):
#     #         user = self.user_dict[message.chat.id]
#     #         user.watchlist = functions.get_user_watchlist(user.username)
#     #         if user.watchlist:
#     #             amount = functions.get_amount_bank_user(user.username)
#     #             timeframe = functions.get_user_timeframe(user.username)
#     #             coins = ""
#     #             for watchlist in user.watchlist:
#     #                 if watchlist[1]:
#     #                     coin = str(functions.get_coin_name(int(watchlist[1])))
#     #                     percent = candle.get_percent_candle(coin, timeframe)
#     #                     percent = str(percent) + " 🔴" if percent < 0 else str(percent) + " 🟢"
#     #                     coins += coin + " %" + percent + "\n"
#     #             # amount = 0
#     #             res = "💰 " + trans('C_assets') + "\n" + str(amount) + "$\n\n👀 " \
#     #                   + trans('C_watchlist') + "\n" + user.watchlist[0][2] + "\n\n💎 " \
#     #                   + trans('C_coin') + "\n" + coins + "\n⏱ " + trans('C_timeframe') + "\n" + timeframe
#     #             self.bot.reply_to(message, res)
#     #         else:
#     #             self.bot.reply_to(message, trans('C_create_watchlist_first'))
#
#     # @self.bot.message_handler(commands=['candle'])
#     # def show_candle(message):
#     #     if self.check_login(message):
#     #         user = self.user_dict[message.chat.id]
#     #         coins = functions.get_user_coins(user.username)
#     #         timeframe = functions.get_user_timeframe(user.username)
#     #         for coin in coins:
#     #             res = candle.candle_details_to_string(coin, timeframe)
#     #             self.bot.reply_to(message, res)
#     #
#     # @self.bot.message_handler(commands=['recommendation'])
#     # def show_recommendation(message):
#     #     if self.check_login(message):
#     #         user = self.user_dict[message.chat.id]
#     #         coins = functions.get_user_coins(user.username)
#     #         timeframe = functions.get_user_timeframe(user.username)
#     #         user.timeframe = timeframe
#     #         for coin in coins:
#     #             recommendation = telebot.types.InlineKeyboardMarkup()
#     #             recom = tr(coin, timeframe, 'summary')[0]
#     #             result = f'{coin}\n' \
#     #                      f'{trans("C_recommendation")} : {recom["RECOMMENDATION"]} \n' \
#     #                      f'{trans("C_buy")} : {recom["BUY"]} \n' \
#     #                      f'{trans("C_sell")} : {recom["SELL"]} \n' \
#     #                      f'{trans("C_neutral")} : {recom["NEUTRAL"]}'
#     #             recommendation.add(
#     #                 telebot.types.InlineKeyboardButton(trans('C_moving_averages'),
#     #                                                    callback_data=f'{coin}_tradingview_MA'),
#     #                 telebot.types.InlineKeyboardButton(trans('C_oscillators'),
#     #                                                    callback_data=f'{coin}_tradingview_OSI'))
#     #             self.bot.send_message(chat_id=message.chat.id, text=result,
#     #                                   reply_markup=recommendation)
#     #
#     # @self.bot.message_handler(commands=['analysis'])
#     # def set_analysis(message):
#     #     if self.check_login(message):
#     #         # if user dont have an analysis
#     #         user = self.user_dict[message.chat.id]
#     #         analysis = functions.get_user_analysis_name(user.username)
#     #         if not analysis:
#     #             analysis_keyboard = telebot.types.InlineKeyboardMarkup()
#     #             for index, analyze in self.analysis_list:
#     #                 analysis_keyboard.add(telebot.types.InlineKeyboardButton(analyze, callback_data=analyze))
#     #             self.bot.send_message(chat_id=message.chat.id, text=trans('C_select_analysis'),
#     #                                   reply_markup=analysis_keyboard)
#     #         else:
#     #             self.bot.reply_to(message, trans('C_already_have_analysis') + analysis)
#     #
#     # """
#     #         removes command handler
#     # """
#     #
#     # @self.bot.message_handler(commands=['remove'])
#     # def remove(message):
#     #     if self.check_login(message):
#     #         try:
#     #             remove_keyboard = telebot.types.InlineKeyboardMarkup()
#     #             remove_keyboard.add(telebot.types.InlineKeyboardButton(trans('C_watchlist'),
#     #                                                                    callback_data="remove_watchlist"),
#     #                                 telebot.types.InlineKeyboardButton(trans('C_coin'),
#     #                                                                    callback_data="remove_coins"),
#     #                                 telebot.types.InlineKeyboardButton(trans('C_analysis'),
#     #                                                                    callback_data="remove_analysis")
#     #                                 )
#     #             self.bot.send_message(chat_id=message.chat.id, text=trans('C_select_option_delete'),
#     #                                   reply_markup=remove_keyboard)
#     #
#     #         except Exception as e:
#     #             self.bot.reply_to(message, trans('C_unsuccessful_operation'))
#     #             print(e)
#
#     @self.bot.message_handler(commands=['help'])
#     def help_me(message):
#         try:
#             self.bot.reply_to(message, trans('C_help'))
#
#         except Exception as e:
#             self.bot.reply_to(message, trans('C_unsuccessful_operation'))
#             print(e)
#
#     @self.bot.message_handler(commands=['guide'])
#     def guide_me(message):
#         try:
#             self.bot.reply_to(message, trans('C_guide'))
#
#         except Exception as e:
#             self.bot.reply_to(message, trans('C_unsuccessful_operation'))
#             print(e)
#
#     """
#         logout command handler
#     """
#
#     @self.bot.message_handler(commands=['logout'])
#     def logout(message):
#         if self.check_login(message):
#             try:
#                 self.user_dict[message.chat.id].session = False
#                 self.bot.reply_to(message, trans('C_goodbye') + '\n' + trans('C_login_again'))
#                 self.user_dict[message.chat.id].login = False
#                 self.user_dict[message.chat.id].session = False
#             except Exception as e:
#                 self.bot.reply_to(message, trans('C_unsuccessful_logout'))
#                 print(e)

