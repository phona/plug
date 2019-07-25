<template>
    <div class="login-wrap">
        <div class="ms-title">欢迎使用云顶之弈棋魂1.0</div>
        <div class="ms-login">

            <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0px">
                <el-form-item prop="code">
                    <el-input v-model="ruleForm.code" :maxlength='36' :minlength='36' placeholder="请输入36位激活码"></el-input>
                </el-form-item>

                <div class="login-btn">
                    <el-button type="primary" @click="submitForm('ruleForm')">确 认</el-button>
                </div>
            </el-form>

        </div>
    </div>
</template>

<script>
	export default {
		name: 'login',

		data() {
			let validateCode = (rule, value, callback) => {
				if (value.length < 36) {
					callback(new Error('激活码不能小于36位'));
				} else {
					callback();
				}
			};

			return {
                activeRequest: {
                    code: '',
                },
                ruleForm: {
                    code: '',
                },
                rules: {
                    code: [
                        {validator: validateCode, trigger: 'blur'}
                    ],
                }
			}
		},

		methods: {
			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
					if (valid) {
						this.activeRequest.code = this.ruleForm.code;
						this.$axios.post('/apis/actives', this.activeRequest)
							.then(resp => {
                                return new Promise((resolve, reject) => {
                                    this.$alert("激活成功", "", {
                                        confirmButtonText: '确定',
                                        callback: action => {
                                            resolve();
                                        }
                                    });
                                });
							})
							.then(_ => {
								this.$router.push("/main");
							})
							.catch(error => {
								this.$message.error(error.response.data.msg);
							});
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
        height: 80px;
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
