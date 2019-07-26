<template>
    <div class="login-wrap">
        <div class="ms-title">欢迎使用云顶之弈棋魂1.0</div>
        <div class="ms-login">
            <el-row :gutter="10" style="margin-bottom: 10px">
                <el-col :offset="20">
                    <el-button icon="el-icon-arrow-right" class="register-text" type="text" @click="$router.push('/register')">注册</el-button>
                </el-col>
            </el-row>

            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px">
                <el-form-item prop="username">
                    <el-input v-model="ruleForm.username" placeholder="用户名"></el-input>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input type="password" placeholder="密 码" v-model="ruleForm.password"
                            @keyup.enter.native="submitForm('ruleForm')"></el-input>
                </el-form-item>

                <div class="login-btn">
                    <el-button type="primary" @click="submitForm('ruleForm')">登录</el-button>
                </div>
            </el-form>

        </div>
    </div>
</template>

<script>
	export default {
		name: 'login',

		data() {
			return {
                loginRequest: {
                    username: '',
                    password: '',
                },
                ruleForm: {
                    username: '',
                    password: '',
                },
                rules: {
                    username: [
                        {required: true, message: '请输入用户名', trigger: 'blur'}
                    ],
                    password: [
                        {required: true, message: '请输入密码', trigger: 'blur'}
                    ]
                }
			}
		},

		methods: {
			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.loginRequest.username = this.ruleForm.username;
						this.loginRequest.password = this.ruleForm.password;
                        this.$axios.post('/apis/login', this.loginRequest)
                            .then((resp) => {
                                const username = this.loginRequest.username;
                                const token = resp.data.access_token;
                                localStorage.setItem('token', token);
                                this.$axios.defaults.headers.common['Authorization'] = token
                                return new Promise((resolve, reject) => {
                                    this.$alert("登录成功", "", {
                                        confirmButtonText: '确定',
                                        callback: action => {
                                            resolve();
                                        }
                                    });
                                });
                            })
                            .then(_ => {
                                return this.$axios.get('/apis/actives');
                            })
                            .then(resp => {
                                this.$router.push('/main');
                            })
                            .catch(error => {
                                if (error.response.data.code === 403) {
                                    this.$router.push('/active');
                                } else if (error.response.data.code === 401) {
                                    this.$message.error("用户名或密码错误");
                                } else if (error.response.data.msg !== undefined) {
                                    this.$message.error(error.response.data.msg);
                                } else {
                                    this.$message.error("未知错误，请联系管理员处理");
                                }
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
        height: 170px;
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
