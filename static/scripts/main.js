(function() {
  window.addEventListener('load', function() {
    var path = window.location.pathname

    if (path === '' || path === '/') {
      addRepoForm()
    }
  })
})()

function addRepoForm() {
  var repo = {
    user: document.querySelector('.form input.repo-user'),
    name: document.querySelector('.form input.repo-name')
  }

  for (var el in repo) {
    repo[el].addEventListener('keyup', function(e) {
      document.querySelector('span.keyword.' + this.classList[0]).innerHTML = this.value
    })
  }

  var submit = document.querySelector('.form input.btn')

  submit.addEventListener('click', function(e) {
    var user = repo.user.value.trim(),
        name = repo.name.value.trim()

    if (!user || !user.length || !name || !name.length) {
      return
    }

    window.location = '/' + repo.user.value + '/' + repo.name.value
  })
}
