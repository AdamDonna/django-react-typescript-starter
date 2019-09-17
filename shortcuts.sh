lint() {
    workingset=$(git diff HEAD --name-only --diff-filter=d)
    committed=$(git diff origin/develop... --name-only --)
    # shellcheck disable=SC2086
    PIPENV_PIPFILE=./Pipfile pipenv run pre-commit run -v --files $workingset $committed
}

cmd="${1:-}"
shift || true

if [[ -z "$cmd" ]]; then
    show_help >&2; exit 1
fi

# map some commands so we can just pass them to manage... for now
case "$cmd" in
    shell) cmd="shell_plus"
        ;;
esac

case "$cmd" in
    logs) docker-compose logs --tail=100 -f "$@"
        ;;
    bash) docker-compose run --rm "${1:-django}" bash
        ;;
    root) docker-compose run --rm --user 0 "${1:-django}" bash
        ;;
    psql) docker-compose exec postgres psql -U postgres postgres
        ;;
    lint) lint
esac