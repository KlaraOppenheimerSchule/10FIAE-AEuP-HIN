<?php

class Character
{
    private string $name;
    private int $health;

    public function __construct(string $name, int $health)
    {
        $this->name = $name;
        $this->health = $health;
    }

    public function getName(): string
    {
        return $this->name;
    }

    public function setName(string $name): void
    {
        $this->name = $name;
    }
}

$c = new Character("Aragorn", 150);

echo $c->getName() . PHP_EOL;

$c->setName("Legolas");

echo $c->getName() . PHP_EOL;

?>
