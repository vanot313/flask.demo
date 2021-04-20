<template>
  <div class="app-container">
    <div v-if="user">
      <el-row :gutter="20">

        <el-col :span="6" :xs="24">
          <user-card :user="user" />
        </el-col>

        <el-col :span="18" :xs="24">
          <el-card>
            <el-tabs v-model="activeTab">
              <el-tab-pane label="活动" name="activity">
                <activity />
              </el-tab-pane>
              <el-tab-pane label="时间线" name="timeline">
                <timeline />
              </el-tab-pane>
              <el-tab-pane label="账号信息" name="account">
                <account :user="user" />
              </el-tab-pane>
            </el-tabs>
          </el-card>
        </el-col>

      </el-row>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import UserCard from './components/UserCard'
import Activity from './components/Activity'
import Timeline from './components/Timeline'
import Account from './components/Account'
import { getInfo } from '@/api/user'

export default {
  name: 'Profile',
  components: { UserCard, Activity, Timeline, Account },
  data() {
    return {
      user: {},
      activeTab: 'activity'
    }
  },
  computed: {
    ...mapGetters([
      'name',
      'avatar',
      'roles',
      'id'
    ])
  },
  created() {
    this.getUser()
  },
  methods: {
    getUser() {
      getInfo().then(response => {
        const { email, mobile, location, birth, description } = response.data

        this.user = {
          id: this.id,
          name: this.name,
          role: this.roles.join(' | '),
          avatar: this.avatar,
          image: require(`@/assets/avatar/` + this.avatar),
          email: email,
          mobile: mobile,
          location: location,
          birth: birth === 'None' ? undefined : birth,
          description: description
        }
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>
