import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NivelDeEnsinoComponent } from './nivelDeEnsino.component';

describe('NivelDeEnsinoComponent', () => {
  let component: NivelDeEnsinoComponent;
  let fixture: ComponentFixture<NivelDeEnsinoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NivelDeEnsinoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NivelDeEnsinoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
