import Vue from 'vue'
import freeModePlay from '@/pages/freeModePlay.vue'
import request from 'XMLHttpRequest'

describe('freeModeUpload.vue', () => {
  const Constructor = Vue.extend(freeModePlay)
  const vm = new Constructor().$mount()
  it('单元测试freeModePlay中的变量和函数', () => {
    expect(vm.dialogVisible).toEqual(false)
    expect(vm.username).toEqual('')
    expect(vm.level).toEqual(1)
    expect(vm.map_id).toEqual(1)
    expect(vm.isRun).toEqual(false)
    expect(vm.workspace).toEqual(null)
    expect(vm.luaEditor).toEqual(false)
    expect(vm.code).toEqual('')
    expect(vm.shareUrl).toEqual('')
    expect(typeof freeModePlay.data).toBe('function')
    expect(typeof freeModePlay.methods.click).toBe('function')
    expect(typeof freeModePlay.methods.myUpdateFunction).toBe('function')
    expect(typeof freeModePlay.methods.run).toBe('function')
    expect(typeof freeModePlay.methods.finish).toBe('function')
    expect(typeof freeModePlay.methods.finish2).toBe('function')
    expect(typeof freeModePlay.methods.restart).toBe('function')
    expect(typeof freeModePlay.methods.getMapData).toBe('function')
    expect(typeof freeModePlay.methods.back).toBe('function')
  })
  it('单元测试freeModePlay中的运行按钮的点击事件', () => {
    let button = vm.$el.querySelector('btn-row')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    freeModePlay._watcher.run()
  })
  it('单元测试freeModePlay中的重新开始按钮的点击事件', () => {
    let button = vm.$el.querySelector('btn-row warning')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    freeModePlay._watcher.run()
  })
  it('单元测试freeModePlay中的完成按钮的点击事件', () => {
    let button = vm.$el.querySelector('btn-nextlevel')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    freeModePlay._watcher.run()
  })
  it('单元测试freeModePlay中的返回按钮的点击事件', () => {
    let button = vm.$el.querySelector('info')
    const clickEvent = new window.Event('click')
    button.dispatchEvent(clickEvent)
    freeModePlay._watcher.run()
  })
  it('异步请求链接分享页面应该返回一个对象', done => {
    request
      .get('http://localhost:8080/shareLink')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
  it('异步请求挑战模式页面应该返回一个对象', done => {
    request
      .get('http://localhost:8080/ChallengeMode/getChallengeMapContent')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
  it('异步请求添加链接分享页面应该返回一个对象', done => {
    request
      .get('http://localhost:8080/ChallengeMode/addShareLink')
      .end(function (err, res) {
        expect(res).to.be.an('object')
        expect(err).to.be.an('object')
        done()
      })
  })
})
