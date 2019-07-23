<template>
	<el-container style="height: 100%; border: 1px solid #eee">
		<el-aside style="height: 100%; background-color: rgb(238, 241, 246)">
			<el-menu>
				<el-submenu :index="k" v-for="(v, k) in heros">
					<template slot="title">
						{{ k }}
					</template>
					<el-menu-item-group>
						<el-menu-item :index="s" v-for="s in v">
							{{ s }}
						</el-menu-item>
					</el-menu-item-group>
				</el-submenu>
			</el-menu>
		</el-aside>
				
		<el-container>
			<el-header style="text-align: right; font-size: 12px">
			<el-dropdown>
				<i class="el-icon-setting" style="margin-right: 15px"></i>
				<el-dropdown-menu slot="dropdown">
				<el-dropdown-item>查看</el-dropdown-item>
				<el-dropdown-item>新增</el-dropdown-item>
				<el-dropdown-item>删除</el-dropdown-item>
				</el-dropdown-menu>
			</el-dropdown>
			<span>王小虎</span>
			</el-header>

			<el-main>
				<el-row :gutter="20">
					<el-col :span="8">
						<el-card style="width: 400px">
							<div slot="header" class="clearfix">
								<span>请根据游戏阵容进行动态调整（建议多选阵容）</span>
							</div>
							<el-main>
								<el-row>
									<el-switch
										v-model="value3"
										active-text="正常概率">
									</el-switch>
								</el-row>
								<el-row>
									<el-switch
										v-model="value3"
										active-text="2倍概率">
									</el-switch>
								</el-row>
								<el-row>
									<el-switch
										v-model="value3"
										active-text="2.5倍概率">
									</el-switch>
								</el-row>
							</el-main>
						</el-card>
					</el-col>

					<el-col :span="8">
						<el-card style="width: 400px">
							<div slot="header" class="clearfix">
								<span>稳定功能区</span>
							</div>
							<el-main>
								<el-row>
									<el-switch
										v-model="value3"
										active-text="增加装备掉落率">
									</el-switch>
								</el-row>
								<el-row>
									<el-switch
										v-model="value3"
										active-text="提升已有棋子概率">
									</el-switch>
								</el-row>
								<el-row>
									<el-switch
										v-model="value3"
										active-text="提升癞子牌概率">
									</el-switch>
								</el-row>
							</el-main>
						</el-card>
					</el-col>

					<el-col :span="8">
						<el-card style="width: 400px">
							<div slot="header" class="clearfix">
								<span>测试功能区</span>
							</div>
							<el-main>
								<el-row>
									<el-switch
										v-model="value3"
										active-text="增加挑打排名靠后(4-8)玩家概率">
									</el-switch>
								</el-row>
								<el-row>
									<el-switch
										v-model="value3"
										active-text="获得死亡玩家装备">
									</el-switch>
								</el-row>
								<el-row>
									<el-switch
										v-model="value3"
										disabled
										active-text="放举报">
									</el-switch>
								</el-row>
							</el-main>
						</el-card>
					</el-col>

				</el-row>
			</el-main>
		</el-container>

	</el-container>
</template>

<script>
	export default {
		data() {
			const item = {
				date: '2016-05-02',
				name: '王小虎',
				address: '上海市普陀区金沙江路 1518 弄'
			};
			return {
				tableData: Array(30).fill(item),
				heros: {},
				value3: false,
			}
		},

		created() {
			this.loadData();
			setInterval(() => {
				this.loadData();
			}, 10000);
		},

		methods: {
			loadData() {
				this.$axios.get("/apis/heros")
					.then(resp => {
						this.heros = resp.data;
						console.log(this.heros);
					})
					.catch(error => {
						if (error.response.data.status_code === 401) {
							this.$router.push("/login");
						} else {
							this.$message.error(error);
						}
					})
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

	.clearfix:before,
	.clearfix:after {
		display: table;
		content: "";
	}
	.clearfix:after {
		clear: both
	}
</style>
