import click
from .models import Spaceship, SpaceshipModule

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug


@cli.command()
@click.argument('file', type=click.File('r'))
@click.pass_context
def day1(ctx, file):
    spaceship = Spaceship()

    for cnt, line in enumerate(file):
        module = SpaceshipModule(name=cnt, weight=int(line.rstrip()))
        spaceship.add_module(module=module)
        if ctx.obj['DEBUG']:
            click.echo(module)

    if ctx.obj['DEBUG']:
        click.echo(spaceship)

    click.echo("The step1 result is : %d" % (spaceship.fuel_modules_requirements, ))
    click.echo("The step2 result is : %d" % (spaceship.fuel_requirements, ))


if __name__ == '__main__':
    cli(obj={})
