(function () {
  window.addEventListener('load', function () {
    var path = window.location.pathname

    if (path === '' || path === '/') {
      addRepoForm()
    }
  })
})()

function addRepoForm () {
  var repo = {
    owner: document.querySelector('.form input.repo-owner'),
    name: document.querySelector('.form input.repo-name')
  }

  for (var el in repo) {
    repo[el].addEventListener('keyup', function (e) {
      document.querySelector('span.keyword.' + this.classList[0]).innerHTML = this.value
    })
  }

  var submit = document.querySelector('.form input.btn')

  submit.addEventListener('click', function (e) {
    var owner = repo.owner.value.trim()
    var name = repo.name.value.trim()

    if (!owner || !owner.length || !name || !name.length) {
      return
    }

    window.location = '/' + repo.owner.value + '/' + repo.name.value
  })
}
