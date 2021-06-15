import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Medio3Component } from './medio3.component';

describe('Medio3Component', () => {
  let component: Medio3Component;
  let fixture: ComponentFixture<Medio3Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ Medio3Component ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(Medio3Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
