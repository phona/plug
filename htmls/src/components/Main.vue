<template>
	<el-container style="height: 100%; border: 1px solid #eee">
		<el-aside style="height: 100%; background-color: rgb(238, 241, 246)">
			<el-menu>
				<el-menu-item :index="k" v-for="(v, k) in heros">
					<div slot="title" @click="currentHeroGroup = v">
						{{ k }}
					</div>
					<!-- <el-menu-item-group>
						<el-menu-item :index="s.name" v-for="s in v" @click="currentHero = s">
							{{ s.name }}
						</el-menu-item>
					</el-menu-item-group> -->
				</el-menu-item>
			</el-menu>
		</el-aside>
				
		<el-container>
			<el-header style="font-size: 12px">
				<div style="text-align: right; ">
					尊敬的<span>{{ username }}</span>欢迎您，您的剩余时长为{{ expired }}小时
				</div>
			</el-header>

			<el-main>
				<el-row :gutter="20">
					<span style="font-size: 18px; font-weight: bold;">当前英雄: </span>
					<span v-for="(v) in currentHeroGroup.names">
						{{ v }}
					</span>
				</el-row>
				<el-row>
					<template v-if="currentHeroGroup.names === undefined" >
						<el-button disabled type="primary" @click="$alert('注入成功')">一键注入</el-button>
					</template>
					<template v-else="">
						<el-button 
							type="primary" 
							@click="handleInject">一键注入</el-button>
					</template>
				</el-row>

					<el-row :span="8">
						<el-card style="width: 400px">
							<div slot="header" class="clearfix">
								<span>请根据游戏阵容进行动态调整（建议多选阵容）</span>
							</div>
							<el-main>
								<el-row>
									<el-switch
										v-model="currentHeroGroup.adjust.s1"
										active-text="正常概率">
									</el-switch>
								</el-row>
								<el-row>
									<el-switch
										v-model="currentHeroGroup.adjust.s2"
										active-text="2倍概率">
									</el-switch>
								</el-row>
								<el-row>
									<el-switch
										v-model="currentHeroGroup.adjust.s3"
										active-text="2.5倍概率">
									</el-switch>
								</el-row>
							</el-main>
						</el-card>
						<div 
							v-if="currentHeroGroup.names === undefined"
							class="el-loading-mask" 
							style="width: 400px" 
							@click="$message.info('请先选择英雄')"></div>
					</el-row>

					<el-row :span="8">
						<el-card style="width: 400px">
							<div slot="header" class="clearfix">
								<span>稳定功能区</span>
							</div>
							<el-main>
								<el-row>
									<el-switch
										v-model="reliableAdjust.r1"
										active-text="增加装备掉落率">
									</el-switch>
								</el-row>
								<el-row>
									<el-switch
										v-model="reliableAdjust.r2"
										active-text="提升已有棋子概率">
									</el-switch>
								</el-row>
								<el-row>
									<el-switch
										v-model="reliableAdjust.r3"
										active-text="提升癞子牌概率">
									</el-switch>
								</el-row>
							</el-main>
						</el-card>
					</el-row>

					<el-row :span="8">
						<el-card style="width: 400px">
							<div slot="header" class="clearfix">
								<span>测试功能区</span>
							</div>
							<el-main>
								<el-row>
									<el-switch
										v-model="testAdjust.t1"
										active-text="增加挑打排名靠后(4-8)玩家概率">
									</el-switch>
								</el-row>
								<!-- <el-row>
									<el-switch
										v-model="testAdjust.t2"
										active-text="获得死亡玩家装备">
									</el-switch>
								</el-row> -->
								<el-row>
									<el-switch
										v-model="testAdjust.t3"
										disabled
										active-text="防举报">
									</el-switch>
								</el-row>
							</el-main>
						</el-card>
					</el-row>
			</el-main>
		</el-container>

	</el-container>
</template>

<script>
	let heroAdjust = {
		s1: false,
		s2: false,
		s3: false,
	};

	export default {
		data() {
			return {
				fullscreenLoading: false,
				heros: {},
				username: "",
				expired: "",
				currentHeroGroup: {
					adjust: {
						s1: false,
						s2: false,
						s3: false,
					}
				},
				currentHero: {
					s1: false,
					s2: false,
					s3: false
				},

				reliableAdjust: {
					r1: false,
					r2: false,
					r3: false
				},

				testAdjust: {
					t1: false,
					t2: false,
					t3: false
				}
			}
		},

		created() {
			this.loadData();
			setInterval(() => {
				this.loadData();
			}, 600000);
		},

		methods: {
			loadData() {
				this.$axios.get("/apis/heros")
					.then(resp => {
						this.heros = resp.data;
						for (let h in this.heros) {
							// let heros = [];
							// this.heros[h].forEach(element => {
							// 	heros.push({
							// 		name: element,
							// 		adjust: Object.assign({}, heroAdjust),
							// 	});
							// });
							// this.heros[h] = heros;
							this.heros[h] = {
								names: this.heros[h],
								adjust: Object.assign({}, heroAdjust)
							}
						}
					})
					.catch(error => {
						if (error.response.data.code === 401) {
							this.$alert("您的剩余时长已不足，感谢您的使用", `尊敬的${this.username}`, {
								confirmButtonText: '确定',
								callback: () => {
									this.$router.push("/login");
								}
							})
						} else {
							this.$message.error(error);
						}
					});
				this.$axios.get("/apis/users")
					.then(resp => {
						this.username = resp.data.data.username;
						this.expired = resp.data.data.expired;
						if (this.expired < 3) {
							this.$alert("您的剩余时长已不足3小时，请及时充值", `尊敬的${this.username}`, {
								confirmButtonText: '确定',
								callback: action => {}
							});
						}
					})	
					.catch(error => {
						if (error.response.data !== undefined) {
							this.$message.error(error.response.data.msg);
						} else {
							this.$message.error(error);
						}
					});
			},

			handleInject() {
				this.$axios.get("/apis/heros")
					.then(resp => {
						this.heros = resp.data;
						for (let h in this.heros) {
							this.heros[h] = {
								names: this.heros[h],
								adjust: Object.assign({}, heroAdjust)
							}
						}
						const loading = this.$loading({
							lock: true,
							text: '加载配置中',
							spinner: 'el-icon-loading',
							background: 'rgba(0, 0, 0, 0.7)'
						});
						setTimeout(() => {
							loading.close();
							this.$alert('注入成功');
						}, Math.random() * 10000);
					})
					.catch(error => {
						if (error.response.data.code === 401) {
							this.$alert("您的剩余时长已不足，感谢您的使用", `尊敬的${this.username}`, {
								confirmButtonText: '确定',
								callback: () => {
									this.$router.push("/login");
								}
							})
						} else {
							this.$message.error(error);
						}
					});
			}
		}

	};
</script>

<style scoped>
	.el-header {
		background-color: #B3C0D1;
		color: #333;
		line-height: 60px;
	}
  
	.el-aside {
		color: #333;
	}

	.el-row {
		margin-bottom: 20px;
	}
	.el-col {
		border-radius: 4px;
	}

	.clearfix:before,
	.clearfix:after {
		display: table;
		content: "";
	}
	.clearfix:after {
		clear: both
	}
</style>
