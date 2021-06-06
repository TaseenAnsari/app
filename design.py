#    Image:
        #source: "assets/bg.png"


helper_string = """
ScreenManager:
    LoginPage:
    ForgetPassword:
    GeneratePassword:
    HomePage:
    
<LoginPage>:
    name: "loginpage"
    Image:
        source: "assets/bg.png"
    Image:
        source: "assets/logo.png"
        pos_hint:{"center_x":.5,"center_y":.85}
        size_hint: 0.3,0.3
    MDLabel:
        text :"Ramchardra Chandravansi University"
        pos_hint: {"center_y": .7}
        font_style: "H6"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0,0,0,1
    MDTextField:
        id : college_id
        hint_text: "College ID"
        normal_color: app.theme_cls.accent_color
        color_active: 1, 0, 0, 1
        pos_hint: {"center_x":.5,"center_y":.5}
        icon_right:"account"
        current_hint_text_color: 0,0,0,1
        color_mode: 'custom'
        line_color_focus: 0, 0, 0, 1
        size_hint_x: 0.8
    MDTextField:
        id: password
        hint_text: "Password"
        pos_hint: {"center_x":.5,"center_y":.4}
        current_hint_text_color: 0,0,0,1
        size_hint_x: 0.8
        password: True
        color_mode: 'custom'
        line_color_focus: 0, 0, 0, 1
    MDIconButton:
        id : passwordicon
        icon : "eye-off"
        pos_hint: {"center_x":0.865 , "center_y":0.41}
        on_release: app.show_hide_password()
    MDRaisedButton:
        text: "Login"
        pos_hint: {"center_x":0.5,"center_y":0.3}
        size_hint_x:0.5
        on_release: app.logincheck()
        on_release: root.manager.current = "homepage"
    MDLabel:
        text :"Do you Forgot?"
        pos_hint: {"center_y": 0.25,"center_x":0.35}
        font_style: "Body2"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0,0,0,1
    MDTextButton:
        text: "Click Here"
        pos_hint: {"center_x":0.54,"center_y":0.25}
        size_hint_x:0.2
        custom_color: 0, 0, 1, 1
        on_release : root.manager.current = 'forget'
        
<ForgetPassword>
    name: 'forget'
    Image:
        source: "assets/bg.png"
    Image:
        source: "assets/logo.png"
        pos_hint:{"center_x":.5,"center_y":.85}
        size_hint: 0.3,0.3
    MDLabel:
        text :"Ramchardra Chandravansi University"
        pos_hint: {"center_y": .7}
        font_style: "H6"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0,0,0,1
    MDTextField:
        hint_text: "College ID"
        normal_color: app.theme_cls.accent_color
        color_active: 1, 0, 0, 1
        pos_hint: {"center_x":.5,"center_y":.5}
        icon_right:"account"
        current_hint_text_color: 0,0,0,1
        color_mode: 'custom'
        line_color_focus: 0, 0, 0, 1
        size_hint_x: 0.8
    MDTextField:
        hint_text: "Registration No"
        pos_hint: {"center_x":.5,"center_y":.4}
        current_hint_text_color: 0,0,0,1
        size_hint_x: 0.8
        color_mode: 'custom'
        line_color_focus: 0, 0, 0, 1
    MDRaisedButton:
        text: "Search Password"
        pos_hint: {"center_x":0.5,"center_y":0.3}
        on_release: root.manager.current = "GP"
<GeneratePassword>
    name: "GP"
    Image:
        source: "assets/bg.png"
    Image:
        source: "assets/logo.png"
        pos_hint:{"center_x":.5,"center_y":.85}
        size_hint: 0.3,0.3
    MDLabel:
        text :"Hello, User_Name"
        pos_hint: {"center_y": .6}
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0,0,0,1
    MDLabel:
        text :"Ramchardra Chandravansi University"
        pos_hint: {"center_y": .7}
        font_style: "H6"
        halign: "center"
        theme_text_color: "Custom"
        text_color: 0,0,0,1
    MDTextField:
        text : "password@123"
        hint_text: "Your Password"
        normal_color: app.theme_cls.accent_color
        color_active: 1, 0, 0, 1
        pos_hint: {"center_x":.5,"center_y":.5}
        icon_right:"eye"
        current_hint_text_color: 0,0,0,1
        color_mode: 'custom'
        line_color_focus: 0, 0, 0, 1
        size_hint_x: 0.8
<HomePage>
    name:"homepage"
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:"vertical"
                    MDToolbar:
                        title: "Ramchandra Chandravanshi University"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    BoxLayout:
                        MDLabel:
                            text:"Notice"
                            valaign:"top"
                        MDCard:
                            padding_y:"1dp"
                            size_hint: None, None
                            size: "400dp", "300dp"
                            pos_hint: {"center_x": .5, "center_y": .1}
                            FitImage:
                                source: "assets/notice.jpeg"
                        MDFlatButton:
                            text:"Routine"
                            valaign:"top"
                        
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                canvas:
                    Color:
                        rgba: app.theme_cls.primary_color
                    Rectangle:
                        pos: self.pos
                        size: self.size
                spacing : '1dp'
                padding: '10dp'
                orientation: 'vertical'
                Image:
                    source: "assets/my.jpg"
                    pos_hint: {"center_x":0.12}
                    size_hint: .25 , .25
                MDLabel:
                    id: stu_name
                    text : "Noor Mohammad"
                    font_style: 'Subtitle1'
                    size_hint_y: None
                    height: self.texture_size[1]
                    
                MDLabel:
                    id: stu_branch
                    text : "ELECTRICAL ENGINEERING"
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    id: stu_roll_no
                    text : "EE190009"
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    id: stu_sess
                    text : "2018-22"
                    font_style: 'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]
                ScrollView:
                    MDList:
                        OneLineAvatarListItem:
                            text: "My Profile"
                            IconLeftWidget:
                                icon: "face-profile"
                        OneLineAvatarListItem:
                            text: "Logout"
                            IconLeftWidget:
                                icon: "logout"
    
        
"""
