import { Component, OnInit } from '@angular/core';
import { observable, Observable } from 'rxjs';
import { SharedService} from 'src/app/shared.service';

@Component({
  selector: 'app-medio3',
  templateUrl: './medio3.component.html',
  styleUrls: ['./medio3.component.css']
})
export class EnsinoMedio3Component implements OnInit {

  constructor(private service:SharedService) { }

  EscolaList:any=[];

  ngOnInit(): void {
    this.refreshDepList();
  }

  refreshDepList() {
    this.service.getEscolaList().subscribe(data=>{
      this.EscolaList=data;
    });
  }

  detail(dataItem: any): void {
    this.service.selectedSchool = dataItem;
  }
}
