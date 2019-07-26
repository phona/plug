<template>
    <div class="login-wrap">
        <div class="ms-title">欢迎使用云顶之弈棋魂1.0</div>
        <div class="ms-login">
            <el-row :gutter="10" style="margin-bottom: 10px">
                <el-col :offset="18">
                    <el-button icon="el-icon-arrow-right" type="text" @click="$router.push('/login')">立即登录</el-button>
                </el-col>
            </el-row>

            <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="0px" class="demo-ruleForm">
                <el-form-item prop="username">
                    <el-input v-model="ruleForm.username" placeholder="用户名"></el-input>
                </el-form-item>

                <el-form-item prop="password">
                    <el-input type="password" placeholder="密 码" v-model="ruleForm.password"></el-input>
                </el-form-item>

                <el-form-item prop="confirmPassword">
                    <el-input type="password" placeholder="确认密码" v-model="ruleForm.confirmPassword"></el-input>
                </el-form-item>

                <el-form-item prop="mail">
                    <el-input placeholder="邮 箱" v-model="ruleForm.mail"></el-input>
                </el-form-item>

				<div class="login-btn">
					<el-button type="primary" @click="submitForm('ruleForm')">注  册</el-button>
				</div>
            </el-form>
        </div>
    </div>
</template>

<script>
	export default {
		name: 'login',

		data() {
			let validatePass = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请输入密码'));
				} else if (value.length < 8) {
					callback(new Error('密码不能小于8位'));
				} else if (value.length > 32) {
					callback(new Error('密码不能大于32位'));
				} else {
					if (this.ruleForm.confirmPassword !== '') {
						console.log("activate comfirm password check");
						this.$refs.ruleForm.validateField('comfirmPassword');
					}
					callback();
				}
			};

			let validatePass2 = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请再次输入密码'));
				} else if (value.length < 8) {
					callback(new Error('密码不能小于8位'));
				} else if (value.length > 32) {
					callback(new Error('密码不能大于32位'));
				} else if (value !== this.ruleForm.password) {
					callback(new Error('两次输入密码不一致!'));
				} else {
					callback();
				}
			};

			let validateEmail = (rule, value, callback) => {
				if (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value))
					callback();
				else
					callback(new Error('非法邮箱'));
			};

			return {
                loginRequest: {
                    username: '',
					password: '',
					mail: ''
                },
                ruleForm: {
                    username: '',
                    password: '',
					confirmPassword: '',
					mail: '',
                },
                rules: {
                    username: [
                        {required: true, message: '请输入用户名', trigger: 'blur'}
                    ],
                    password: [
                        {validator: validatePass, trigger: 'blur'}
					],
					confirmPassword: [
						{validator: validatePass2, trigger: 'blur'}
					],
					mail: [
						{validator: validateEmail, trigger: 'blur'}
					],
                }
			}
		},

		methods: {
			checkForm(e) {
				this.errors = [];
				if (this.ruleForm.password !== this.ruleForm.password) {
					this.errors.push("两次密码不匹配");
				}
				e.preventDefault();
			},

			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.loginRequest.username = this.ruleForm.username;
						this.loginRequest.password = this.ruleForm.password;
						this.loginRequest.mail = this.ruleForm.mail
                        this.$axios.post('/apis/register', this.loginRequest)
                            .then((resp) => {
                                this.$alert("注册成功", "", {
                                    confirmButtonText: '确定',
                                    callback: action => {
                                        this.$router.push('/login');
                                    }
                                });
                                return true;
                            })
                            .catch(error => {
                                this.$message.error(error.response.data.msg);
                            });
						return false;
					} else {
						return false;
					}
				});
			},
		}
	}
</script>

<style scoped>
    .login-wrap {
        position: relative;
        width: 100%;
        height: 100%;
    }

    .ms-title {
        position: absolute;
        top: 50%;
        width: 100%;
        margin-top: -230px;
        text-align: center;
        font-size: 30px;
        color: #fff;

    }

    .ms-login {
        position: absolute;
        left: 50%;
        top: 50%;
        width: 300px;
        height: 280px;
        margin: -150px 0 0 -190px;
        padding: 40px;
        border-radius: 5px;
        background: #fff;
    }

    .login-btn {
        text-align: center;
    }

    .login-btn button {
        width: 100%;
        height: 36px;
    }
</style>
