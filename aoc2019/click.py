import click
from .models import Spaceship, SpaceshipModule, GravityAssist


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


@cli.command()
@click.argument('file', type=click.File('r'))
@click.pass_context
def day2(ctx, file):
    data = file.read()
    ga = GravityAssist(input=data)
    ga.set_noun(12)
    ga.set_verb(2)
    ga.compute()

    click.echo('The step1 result is : %s' % (ga.output_value(),))

    output_value = 19690720
    for x in range(0, 99):
        for y in range(0, 99):
            ga.reset()
            ga.set_verb(x)
            ga.set_noun(y)
            ga.compute()
            if ga.output_value() == output_value:
                result = (100 * ga.noun) + ga.verb
                click.echo('The step2 result is : %d' % (result, ))
                break


if __name__ == '__main__':
    cli(obj={})
